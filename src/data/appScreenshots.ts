import type { ImageMetadata } from 'astro';

const framedImages = import.meta.glob<{ default: ImageMetadata }>(
	'../assets/images/framed/*_framed.{png,webp}',
	{ eager: true },
);

function framedImage(name: string) {
	const image = framedImages[`../assets/images/framed/${name}`]?.default;

	if (!image) {
		throw new Error(`Missing framed screenshot asset: ${name}`);
	}

	return image;
}

export interface AppScreenshot {
	id: string;
	light: ImageMetadata;
	lightWebp: ImageMetadata;
	dark: ImageMetadata;
	darkWebp: ImageMetadata;
	captionKey: string;
	alt: string;
}

export const handPlayerScreenshot = {
	light: framedImage('hand_phone_mix_player_light_framed.png'),
	lightWebp: framedImage('hand_phone_mix_player_light_framed.webp'),
	dark: framedImage('hand_phone_mix_player_dark_framed.png'),
	darkWebp: framedImage('hand_phone_mix_player_dark_framed.webp'),
};

export const appScreenshots: AppScreenshot[] = [
	{
		id: 'player',
		light: framedImage('phone_mix_player_light_framed.png'),
		lightWebp: framedImage('phone_mix_player_light_framed.webp'),
		dark: framedImage('phone_mix_player_dark_framed.png'),
		darkWebp: framedImage('phone_mix_player_dark_framed.webp'),
		captionKey: 'screenshots.player',
		alt: 'MindState player with lock-screen controls and mix artwork',
	},
	{
		id: 'mixes',
		light: framedImage('phone_mix_browser_light_framed.png'),
		lightWebp: framedImage('phone_mix_browser_light_framed.webp'),
		dark: framedImage('phone_mix_browser_dark_framed.png'),
		darkWebp: framedImage('phone_mix_browser_dark_framed.webp'),
		captionKey: 'screenshots.mixes',
		alt: 'Mixes library with included and custom mixes by category',
	},
	{
		id: 'beatPicker',
		light: framedImage('phone_tone_editor_light_framed.png'),
		lightWebp: framedImage('phone_tone_editor_light_framed.webp'),
		dark: framedImage('phone_tone_editor_dark_framed.png'),
		darkWebp: framedImage('phone_tone_editor_dark_framed.webp'),
		captionKey: 'screenshots.beatPicker',
		alt: 'Beat picker with brainwave bands and Solfeggio tones',
	},
	{
		id: 'quickEditor',
		light: framedImage('phone_quick_mix_editor_light_framed.png'),
		lightWebp: framedImage('phone_quick_mix_editor_light_framed.webp'),
		dark: framedImage('phone_quick_mix_editor_dark_framed.png'),
		darkWebp: framedImage('phone_quick_mix_editor_dark_framed.webp'),
		captionKey: 'screenshots.quickEditor',
		alt: 'Quick editor with four mix slots',
	},
	{
		id: 'shareQr',
		light: framedImage('phone_qr_display_light_framed.png'),
		lightWebp: framedImage('phone_qr_display_light_framed.webp'),
		dark: framedImage('phone_qr_display_dark_framed.png'),
		darkWebp: framedImage('phone_qr_display_dark_framed.webp'),
		captionKey: 'screenshots.shareQr',
		alt: 'Share screen with branded QR code for mix sharing',
	},
	{
		id: 'addTrack',
		light: framedImage('phone_add_track_modal_light_framed.png'),
		lightWebp: framedImage('phone_add_track_modal_light_framed.webp'),
		dark: framedImage('phone_add_track_modal_dark_framed.png'),
		darkWebp: framedImage('phone_add_track_modal_dark_framed.webp'),
		captionKey: 'screenshots.addTrack',
		alt: 'Full editor add-track sheet with tone, noise, effect, and file types',
	},
	{
		id: 'fullEditor',
		light: framedImage('phone_full_mix_editor_light_framed.png'),
		lightWebp: framedImage('phone_full_mix_editor_light_framed.webp'),
		dark: framedImage('phone_full_mix_editor_dark_framed.png'),
		darkWebp: framedImage('phone_full_mix_editor_dark_framed.webp'),
		captionKey: 'screenshots.fullEditor',
		alt: 'Full editor with volume envelopes and track controls',
	},
	{
		id: 'ritualsList',
		light: framedImage('phone_rituals_list_light_framed.png'),
		lightWebp: framedImage('phone_rituals_list_light_framed.webp'),
		dark: framedImage('phone_rituals_list_dark_framed.png'),
		darkWebp: framedImage('phone_rituals_list_dark_framed.webp'),
		captionKey: 'screenshots.ritualsList',
		alt: 'Daily Rituals list with scheduled mixes',
	},
	{
		id: 'ritualEdit',
		light: framedImage('phone_ritual_edit_light_framed.png'),
		lightWebp: framedImage('phone_ritual_edit_light_framed.webp'),
		dark: framedImage('phone_ritual_edit_dark_framed.png'),
		darkWebp: framedImage('phone_ritual_edit_dark_framed.webp'),
		captionKey: 'screenshots.ritualEdit',
		alt: 'Ritual editor with time, repeat days, and linked mix',
	},
];

export const featuredScreenshotIds = ['player', 'mixes', 'beatPicker', 'addTrack'];
