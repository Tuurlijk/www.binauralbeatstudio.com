import type { Locale } from '../i18n/types';

const OG_LOCALE_MAP: Record<Locale, string> = {
	en: 'en_US',
	ar: 'ar_SA',
	es: 'es_ES',
	hi: 'hi_IN',
	id: 'id_ID',
	ja: 'ja_JP',
	nl: 'nl_NL',
	pt: 'pt_BR',
	ru: 'ru_RU',
	zh: 'zh_CN',
};

const SCHEMA_LANGUAGE_MAP: Record<Locale, string> = {
	en: 'en-US',
	ar: 'ar-SA',
	es: 'es-ES',
	hi: 'hi-IN',
	id: 'id-ID',
	ja: 'ja-JP',
	nl: 'nl-NL',
	pt: 'pt-BR',
	ru: 'ru-RU',
	zh: 'zh-CN',
};

export function getOgLocale(locale: Locale): string {
	return OG_LOCALE_MAP[locale] ?? 'en_US';
}

export function getSchemaLanguage(locale: Locale): string {
	return SCHEMA_LANGUAGE_MAP[locale] ?? 'en-US';
}
