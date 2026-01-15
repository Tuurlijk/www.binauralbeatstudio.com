// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import { i18n, filterSitemapByDefaultLocale } from 'astro-i18n-aut/integration';
import sitemap from '@astrojs/sitemap';

const locales = {
  en: 'en-US',
  ar: 'ar-SA',
  es: 'es-ES',
  hi: 'hi-IN',
  id: 'id-ID',
  nl: 'nl-NL',
  pt: 'pt-BR',
  ru: 'ru-RU',
  zh: 'zh-CN',
};

// https://astro.build/config
export default defineConfig({
  base: '/',
  output: 'static',
  site: 'https://binauralbeatstudio.com',
  trailingSlash: 'always',
  build: {
    format: 'directory',
  },
  devToolbar: {
    enabled: false, // Disable dev toolbar to prevent perf.js from reloading images
  },
  integrations: [
    i18n({
      locales,
      defaultLocale: 'en',
      redirectDefaultLocale: false, // Keep /en/ in URL for consistency
    }),
    sitemap({
      i18n: {
        locales,
        defaultLocale: 'en',
      },
      filter: filterSitemapByDefaultLocale({ defaultLocale: 'en' }),
    }),
  ],
  vite: {
    plugins: [tailwindcss()]
  }
});