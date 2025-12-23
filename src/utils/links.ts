import type { Locale } from '../i18n/types';

/**
 * Get localized link with locale prefix
 */
export function getLocalizedLink(path: string, locale: Locale, base: string = ''): string {
  // Remove leading slash if present
  const cleanPath = path.startsWith('/') ? path.slice(1) : path;
  // Ensure base doesn't end with / and doesn't create double slashes
  const cleanBase = base === '/' ? '' : base.replace(/\/$/, '');
  // English (default locale) should use root path, not /en/
  if (locale === 'en') {
    return `${cleanBase}/${cleanPath}`;
  }
  // Ensure locale prefix
  return `${cleanBase}/${locale}/${cleanPath}`;
}

/**
 * Get localized hash link (for anchor links)
 */
export function getLocalizedHashLink(hash: string, locale: Locale, base: string = ''): string {
  // Remove leading # if present, we'll add it back
  const cleanHash = hash.startsWith('#') ? hash.slice(1) : hash;
  // Ensure base doesn't end with / and doesn't create double slashes
  const cleanBase = base === '/' ? '' : base.replace(/\/$/, '');
  // English (default locale) should use root path, not /en/
  if (locale === 'en') {
    return `${cleanBase}/#${cleanHash}`;
  }
  return `${cleanBase}/${locale}/#${cleanHash}`;
}

