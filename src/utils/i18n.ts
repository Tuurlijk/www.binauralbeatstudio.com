import { getRelativeLocaleUrl } from 'astro:i18n';
import type { Locale } from '../i18n/types';
import enTranslations from '../i18n/en.json';

type TranslationKey = string;
type TranslationParams = Record<string, string | number>;

// Cache for loaded translations
const translationCache: Partial<Record<Locale, any>> = {
  en: enTranslations,
};

// Dynamic imports for other locales
const translationLoaders: Record<Locale, () => Promise<any>> = {
  en: async () => enTranslations,
  ar: () => import('../i18n/ar.json'),
  es: () => import('../i18n/es.json'),
  hi: () => import('../i18n/hi.json'),
  id: () => import('../i18n/id.json'),
  ja: () => import('../i18n/ja.json'),
  nl: () => import('../i18n/nl.json'),
  pt: () => import('../i18n/pt.json'),
  ru: () => import('../i18n/ru.json'),
  zh: () => import('../i18n/zh.json'),
};

/**
 * Load translations for a given locale with caching
 */
export async function loadTranslations(locale: Locale): Promise<any> {
  if (translationCache[locale]) {
    return translationCache[locale];
  }
  
  try {
    const module = await translationLoaders[locale]();
    const translations = module.default || module;
    translationCache[locale] = translations;
    return translations;
  } catch (error) {
    console.warn(`Failed to load translations for ${locale}, falling back to English`);
    return enTranslations;
  }
}

/**
 * Get nested value from object using dot notation path
 */
export function getNestedValue(obj: any, path: string): string | undefined {
  return path.split('.').reduce((current, key) => {
    if (current && typeof current === 'object' && key in current) {
      return current[key];
    }
    return undefined;
  }, obj);
}

/**
 * Translate a key with optional parameters
 */
export function t(
  key: TranslationKey,
  locale: Locale,
  translations: any,
  params?: TranslationParams
): string {
  let translation = getNestedValue(translations, key);
  
  // Fallback to English if translation missing
  if (!translation || translation === key) {
    translation = getNestedValue(enTranslations, key);
  }
  
  // Final fallback to key itself
  if (!translation) {
    console.warn(`Translation missing for key: ${key} in locale: ${locale}`);
    return key;
  }
  
  // Replace parameters in translation
  if (params && typeof translation === 'string') {
    return translation.replace(/\{(\w+)\}/g, (match, paramKey) => {
      return params[paramKey]?.toString() || match;
    });
  }
  
  return translation as string;
}

/**
 * Page path without locale prefix (e.g. "/es/demo/" -> "demo", "/" -> "")
 */
export function getPagePathFromUrl(pathname: string): string {
  const withoutLocale = pathname.replace(/^\/(ar|es|hi|id|ja|nl|pt|ru|zh)(?=\/|$)/, '');
  return withoutLocale.replace(/^\/|\/$/g, '');
}

/**
 * Get localized link with locale prefix
 */
export function getLocalizedLink(path: string, locale: Locale): string {
  const cleanPath = path.replace(/^\//, '').replace(/\/$/, '');
  return getRelativeLocaleUrl(locale, cleanPath);
}

/**
 * Get localized hash link (for anchor links)
 */
export function getLocalizedHashLink(hash: string, locale: Locale): string {
  const cleanHash = hash.replace(/^#/, '');
  const baseUrl = getRelativeLocaleUrl(locale, '');
  return `${baseUrl}#${cleanHash}`;
}

