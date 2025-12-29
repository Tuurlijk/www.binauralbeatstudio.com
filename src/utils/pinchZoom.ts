/**
 * Pinch-to-zoom utility for touch and mouse interactions
 * Supports both touch gestures (pinch) and mouse wheel zoom
 */

export interface PinchZoomOptions {
	minScale?: number;
	maxScale?: number;
	initialScale?: number;
	onZoom?: (scale: number) => void;
	onPan?: (x: number, y: number) => void;
}

export class PinchZoom {
	private element: HTMLElement;
	private minScale: number;
	private maxScale: number;
	private scale: number = 1;
	private translateX: number = 0;
	private translateY: number = 0;
	private lastTouchDistance: number = 0;
	private lastTouchCenter: { x: number; y: number } | null = null;
	private isPinching: boolean = false;
	private onZoom?: (scale: number) => void;
	private onPan?: (x: number, y: number) => void;

	constructor(element: HTMLElement, options: PinchZoomOptions = {}) {
		this.element = element;
		this.minScale = options.minScale ?? 0.5;
		this.maxScale = options.maxScale ?? 5;
		this.scale = options.initialScale ?? 1;
		this.onZoom = options.onZoom;
		this.onPan = options.onPan;

		this.init();
	}

	private init() {
		this.element.style.touchAction = 'none';
		this.element.style.userSelect = 'none';
		this.element.style.transformOrigin = '0 0';
		
		this.updateTransform();

		// Touch events
		this.element.addEventListener('touchstart', this.handleTouchStart.bind(this), { passive: false });
		this.element.addEventListener('touchmove', this.handleTouchMove.bind(this), { passive: false });
		this.element.addEventListener('touchend', this.handleTouchEnd.bind(this), { passive: false });
		this.element.addEventListener('touchcancel', this.handleTouchEnd.bind(this), { passive: false });

		// Mouse wheel zoom
		this.element.addEventListener('wheel', this.handleWheel.bind(this), { passive: false });

		// Pan with mouse drag
		let isDragging = false;
		let lastMouseX = 0;
		let lastMouseY = 0;

		this.element.addEventListener('mousedown', (e) => {
			if (e.button === 0 && !this.isPinching) {
				isDragging = true;
				lastMouseX = e.clientX;
				lastMouseY = e.clientY;
				this.element.style.cursor = 'grabbing';
			}
		});

		document.addEventListener('mousemove', (e) => {
			if (isDragging && !this.isPinching) {
				const deltaX = e.clientX - lastMouseX;
				const deltaY = e.clientY - lastMouseY;
				this.translateX += deltaX / this.scale;
				this.translateY += deltaY / this.scale;
				this.updateTransform();
				this.onPan?.(this.translateX, this.translateY);
				lastMouseX = e.clientX;
				lastMouseY = e.clientY;
			}
		});

		document.addEventListener('mouseup', () => {
			if (isDragging) {
				isDragging = false;
				this.element.style.cursor = 'grab';
			}
		});

		this.element.style.cursor = 'grab';
	}

	private getTouchDistance(touches: TouchList): number {
		if (touches.length < 2) return 0;
		const dx = touches[0].clientX - touches[1].clientX;
		const dy = touches[0].clientY - touches[1].clientY;
		return Math.sqrt(dx * dx + dy * dy);
	}

	private getTouchCenter(touches: TouchList): { x: number; y: number } {
		if (touches.length === 0) return { x: 0, y: 0 };
		if (touches.length === 1) {
			const rect = this.element.getBoundingClientRect();
			return {
				x: touches[0].clientX - rect.left,
				y: touches[0].clientY - rect.top,
			};
		}
		const x = (touches[0].clientX + touches[1].clientX) / 2;
		const y = (touches[0].clientY + touches[1].clientY) / 2;
		const rect = this.element.getBoundingClientRect();
		return {
			x: x - rect.left,
			y: y - rect.top,
		};
	}

	private handleTouchStart(e: TouchEvent) {
		if (e.touches.length === 2) {
			this.isPinching = true;
			this.lastTouchDistance = this.getTouchDistance(e.touches);
			this.lastTouchCenter = this.getTouchCenter(e.touches);
			e.preventDefault();
		}
	}

	private handleTouchMove(e: TouchEvent) {
		if (e.touches.length === 2 && this.isPinching) {
			const distance = this.getTouchDistance(e.touches);
			const center = this.getTouchCenter(e.touches);

			if (this.lastTouchDistance > 0 && this.lastTouchCenter) {
				const scaleChange = distance / this.lastTouchDistance;
				const newScale = Math.max(this.minScale, Math.min(this.maxScale, this.scale * scaleChange));

				// Calculate zoom center in element coordinates
				const zoomCenterX = center.x / this.scale - this.translateX;
				const zoomCenterY = center.y / this.scale - this.translateY;

				// Adjust translation to keep zoom center fixed
				this.translateX = center.x / newScale - zoomCenterX;
				this.translateY = center.y / newScale - zoomCenterY;

				this.scale = newScale;
				this.updateTransform();
				this.onZoom?.(this.scale);
			}

			this.lastTouchDistance = distance;
			this.lastTouchCenter = center;
			e.preventDefault();
		} else if (e.touches.length === 1 && !this.isPinching) {
			// Single touch pan
			const touch = e.touches[0];
			const rect = this.element.getBoundingClientRect();
			const x = touch.clientX - rect.left;
			const y = touch.clientY - rect.top;
			
			if (this.lastTouchCenter) {
				const deltaX = (x - this.lastTouchCenter.x) / this.scale;
				const deltaY = (y - this.lastTouchCenter.y) / this.scale;
				this.translateX += deltaX;
				this.translateY += deltaY;
				this.updateTransform();
				this.onPan?.(this.translateX, this.translateY);
			}
			
			this.lastTouchCenter = { x, y };
		}
	}

	private handleTouchEnd(e: TouchEvent) {
		if (e.touches.length < 2) {
			this.isPinching = false;
			this.lastTouchDistance = 0;
			if (e.touches.length === 0) {
				this.lastTouchCenter = null;
			}
		}
	}

	private handleWheel(e: WheelEvent) {
		e.preventDefault();
		
		const rect = this.element.getBoundingClientRect();
		const x = e.clientX - rect.left;
		const y = e.clientY - rect.top;

		const zoomFactor = e.deltaY > 0 ? 0.9 : 1.1;
		const newScale = Math.max(this.minScale, Math.min(this.maxScale, this.scale * zoomFactor));

		// Calculate zoom center in element coordinates
		const zoomCenterX = x / this.scale - this.translateX;
		const zoomCenterY = y / this.scale - this.translateY;

		// Adjust translation to keep zoom center fixed
		this.translateX = x / newScale - zoomCenterX;
		this.translateY = y / newScale - zoomCenterY;

		this.scale = newScale;
		this.updateTransform();
		this.onZoom?.(this.scale);
	}

	private updateTransform() {
		this.element.style.transform = `translate(${this.translateX}px, ${this.translateY}px) scale(${this.scale})`;
	}

	public setScale(scale: number) {
		this.scale = Math.max(this.minScale, Math.min(this.maxScale, scale));
		this.updateTransform();
		this.onZoom?.(this.scale);
	}

	public setTranslate(x: number, y: number) {
		this.translateX = x;
		this.translateY = y;
		this.updateTransform();
		this.onPan?.(x, y);
	}

	public reset() {
		this.scale = 1;
		this.translateX = 0;
		this.translateY = 0;
		this.updateTransform();
		this.onZoom?.(this.scale);
		this.onPan?.(0, 0);
	}

	public getScale(): number {
		return this.scale;
	}

	public getTranslate(): { x: number; y: number } {
		return { x: this.translateX, y: this.translateY };
	}

	public destroy() {
		this.element.style.touchAction = '';
		this.element.style.userSelect = '';
		this.element.style.transform = '';
		this.element.style.transformOrigin = '';
		this.element.style.cursor = '';
	}
}
