import type { ImageMetadata } from 'astro';

import phoneMixPlayerLight from '../assets/images/phone_mix_player_light.png';
import phoneMixPlayerDark from '../assets/images/phone_mix_player_dark.png';
import phoneMixBrowserLight from '../assets/images/phone_mix_browser_light.png';
import phoneMixBrowserDark from '../assets/images/phone_mix_browser_dark.png';
import phoneToneEditorLight from '../assets/images/phone_tone_editor_light.png';
import phoneToneEditorDark from '../assets/images/phone_tone_editor_dark.png';
import phoneQuickMixEditorLight from '../assets/images/phone_quick_mix_editor_light.png';
import phoneQuickMixEditorDark from '../assets/images/phone_quick_mix_editor_dark.png';
import phoneQrDisplayLight from '../assets/images/phone_qr_display_light.png';
import phoneQrDisplayDark from '../assets/images/phone_qr_display_dark.png';
import phoneAddTrackModalLight from '../assets/images/phone_add_track_modal_light.png';
import phoneAddTrackModalDark from '../assets/images/phone_add_track_modal_dark.png';
import phoneFullMixEditorLight from '../assets/images/phone_full_mix_editor_light.png';
import phoneFullMixEditorDark from '../assets/images/phone_full_mix_editor_dark.png';
import phoneRitualsListLight from '../assets/images/phone_rituals_list_light.png';
import phoneRitualsListDark from '../assets/images/phone_rituals_list_dark.png';
import phoneRitualEditLight from '../assets/images/phone_ritual_edit_light.png';
import phoneRitualEditDark from '../assets/images/phone_ritual_edit_dark.png';

export interface AppScreenshot {
	id: string;
	light: ImageMetadata;
	dark: ImageMetadata;
	captionKey: string;
	alt: string;
}

export const appScreenshots: AppScreenshot[] = [
	{
		id: 'player',
		light: phoneMixPlayerLight,
		dark: phoneMixPlayerDark,
		captionKey: 'screenshots.player',
		alt: 'MindState player with lock-screen controls and mix artwork',
	},
	{
		id: 'mixes',
		light: phoneMixBrowserLight,
		dark: phoneMixBrowserDark,
		captionKey: 'screenshots.mixes',
		alt: 'Mixes library with included and custom mixes by category',
	},
	{
		id: 'beatPicker',
		light: phoneToneEditorLight,
		dark: phoneToneEditorDark,
		captionKey: 'screenshots.beatPicker',
		alt: 'Beat picker with brainwave bands and Solfeggio tones',
	},
	{
		id: 'quickEditor',
		light: phoneQuickMixEditorLight,
		dark: phoneQuickMixEditorDark,
		captionKey: 'screenshots.quickEditor',
		alt: 'Quick editor with four mix slots',
	},
	{
		id: 'shareQr',
		light: phoneQrDisplayLight,
		dark: phoneQrDisplayDark,
		captionKey: 'screenshots.shareQr',
		alt: 'Share screen with branded QR code for mix sharing',
	},
	{
		id: 'addTrack',
		light: phoneAddTrackModalLight,
		dark: phoneAddTrackModalDark,
		captionKey: 'screenshots.addTrack',
		alt: 'Full editor add-track sheet with tone, noise, effect, and file types',
	},
	{
		id: 'fullEditor',
		light: phoneFullMixEditorLight,
		dark: phoneFullMixEditorDark,
		captionKey: 'screenshots.fullEditor',
		alt: 'Full editor with volume envelopes and track controls',
	},
	{
		id: 'ritualsList',
		light: phoneRitualsListLight,
		dark: phoneRitualsListDark,
		captionKey: 'screenshots.ritualsList',
		alt: 'Daily Rituals list with scheduled mixes',
	},
	{
		id: 'ritualEdit',
		light: phoneRitualEditLight,
		dark: phoneRitualEditDark,
		captionKey: 'screenshots.ritualEdit',
		alt: 'Ritual editor with time, repeat days, and linked mix',
	},
];

export const featuredScreenshotIds = ['player', 'mixes', 'beatPicker', 'addTrack'];
