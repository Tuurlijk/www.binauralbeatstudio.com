// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

const localeCodes = ['en', 'ar', 'es', 'hi', 'id', 'nl', 'pt', 'ru', 'zh'];

const sitemapLocales = {
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
  i18n: {
    locales: localeCodes,
    defaultLocale: 'en',
    routing: {
      prefixDefaultLocale: false,
      redirectToDefaultLocale: false,
    },
  },
  devToolbar: {
    enabled: false,
  },
  integrations: [
    sitemap({
      i18n: {
        locales: sitemapLocales,
        defaultLocale: 'en',
      },
    }),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
});
