#!/usr/bin/env node
import { mkdir } from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';

const imageDir = 'src/assets/images';
const outputDir = path.join(imageDir, 'framed');
const handTemplate = path.join(imageDir, 'hand_met_telefoon.png');

const screenshots = [
	'phone_mix_player',
	'phone_mix_browser',
	'phone_tone_editor',
	'phone_quick_mix_editor',
	'phone_qr_display',
	'phone_add_track_modal',
	'phone_full_mix_editor',
	'phone_rituals_list',
	'phone_ritual_edit',
];

const themes = ['light', 'dark'];

const frame = {
	width: 1440,
	height: 2948,
	outerX: 10,
	outerY: 10,
	outerWidth: 1420,
	outerHeight: 2928,
	outerRadius: 132,
	screenX: 48,
	screenY: 48,
	screenWidth: 1344,
	screenHeight: 2856,
	screenRadius: 108,
};

const phoneInHand = {
	x: 748,
	y: 58,
	width: 1140,
};

function svgFrameBase() {
	const {
		width,
		height,
		outerX,
		outerY,
		outerWidth,
		outerHeight,
		outerRadius,
		screenX,
		screenY,
		screenWidth,
		screenHeight,
		screenRadius,
	} = frame;

	return Buffer.from(`
		<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
			<defs>
				<linearGradient id="edge" x1="0" x2="1" y1="0" y2="1">
					<stop offset="0" stop-color="#364147"/>
					<stop offset="0.45" stop-color="#12181c"/>
					<stop offset="1" stop-color="#050709"/>
				</linearGradient>
			</defs>
			<rect x="${outerX}" y="${outerY}" width="${outerWidth}" height="${outerHeight}" rx="${outerRadius}" fill="url(#edge)"/>
			<rect x="${screenX - 10}" y="${screenY - 10}" width="${screenWidth + 20}" height="${screenHeight + 20}" rx="${screenRadius + 20}" fill="#050709"/>
		</svg>
	`);
}

function svgFrameOverlay() {
	const {
		width,
		height,
		outerX,
		outerY,
		outerWidth,
		outerHeight,
		outerRadius,
	} = frame;

	return Buffer.from(`
		<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
			<rect x="${outerX + 20}" y="${outerY + 20}" width="${outerWidth - 40}" height="${outerHeight - 40}" rx="${outerRadius - 24}" fill="none" stroke="rgba(255,255,255,0.16)" stroke-width="8"/>
			<rect x="604" y="68" width="232" height="68" rx="34" fill="#050709"/>
			<circle cx="792" cy="102" r="15" fill="#101820"/>
			<circle cx="797" cy="97" r="5" fill="#243849"/>
			<rect x="${outerX - 8}" y="560" width="12" height="150" rx="6" fill="#11171b"/>
			<rect x="${outerX - 8}" y="770" width="12" height="220" rx="6" fill="#11171b"/>
			<rect x="${outerX + outerWidth - 4}" y="710" width="12" height="270" rx="6" fill="#11171b"/>
		</svg>
	`);
}

function roundedMask(width, height, radius) {
	return Buffer.from(`
		<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
			<rect width="${width}" height="${height}" rx="${radius}" fill="#fff"/>
		</svg>
	`);
}

async function buildFramedPhone(input) {
	const screen = await sharp(input)
		.resize(frame.screenWidth, frame.screenHeight, { fit: 'cover', position: 'top' })
		.composite([{ input: roundedMask(frame.screenWidth, frame.screenHeight, frame.screenRadius), blend: 'dest-in' }])
		.png()
		.toBuffer();

	const pngBuffer = await sharp({
		create: {
			width: frame.width,
			height: frame.height,
			channels: 4,
			background: { r: 0, g: 0, b: 0, alpha: 0 },
		},
	})
		.composite([
			{ input: svgFrameBase(), left: 0, top: 0 },
			{ input: screen, left: frame.screenX, top: frame.screenY },
			{ input: svgFrameOverlay(), left: 0, top: 0 },
		])
		.png()
		.toBuffer();

	return pngBuffer;
}

async function frameScreenshot(baseName, theme) {
	const input = path.join(imageDir, `${baseName}_${theme}.png`);
	const outputBase = path.join(outputDir, `${baseName}_${theme}_framed`);
	const pngBuffer = await buildFramedPhone(input);

	await sharp(pngBuffer).png().toFile(`${outputBase}.png`);
	await sharp(pngBuffer).webp({ quality: 86 }).toFile(`${outputBase}.webp`);
	console.log(`framed ${outputBase}.png`);
}

async function frameHandPlayer(theme) {
	const input = path.join(imageDir, `phone_mix_player_${theme}.png`);
	const outputBase = path.join(outputDir, `hand_phone_mix_player_${theme}_framed`);
	const framedPhone = await sharp(await buildFramedPhone(input))
		.resize({ width: phoneInHand.width })
		.png()
		.toBuffer();

	const pngBuffer = await sharp(handTemplate)
		.composite([{ input: framedPhone, left: phoneInHand.x, top: phoneInHand.y }])
		.png()
		.toBuffer();

	await sharp(pngBuffer).png().toFile(`${outputBase}.png`);
	await sharp(pngBuffer).webp({ quality: 86 }).toFile(`${outputBase}.webp`);
	console.log(`framed ${outputBase}.png`);
}

await mkdir(outputDir, { recursive: true });

for (const theme of themes) {
	for (const screenshot of screenshots) {
		await frameScreenshot(screenshot, theme);
	}

	await frameHandPlayer(theme);
}
