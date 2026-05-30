# MindState website

Marketing site for [Binaural Beat Studio](https://binauralbeatstudio.com), built with **Astro 6** and **Tailwind CSS 4**.

## Requirements

- Node **22.12.0+** (see `.nvmrc`)
- npm

## Commands

| Command | Action |
|---------|--------|
| `npm install` | Install dependencies |
| `npm run dev` | Dev server at `localhost:4321` |
| `npm run build` | Production build to `dist/` |
| `npm run preview` | Preview the production build |

## Project layout

```text
src/
  components/       # UI sections (Hero, Features, …)
  i18n/             # Translation JSON per locale
  layouts/          # Shared Layout.astro
  pages/
    _templates/     # Shared page bodies (not routed directly)
    index.astro     # English home (/)
    demo.astro      # English demo (/demo/)
    es/, nl/, …      # Locale wrappers → /es/, /nl/, …
  utils/i18n.ts     # t(), link helpers
```

## Internationalization

The site supports 9 languages. English uses the root URL (`/`); other locales are prefixed (`/es/`, `/nl/`, …).

**Adding a language or page?** See [features/multi-language-i18n-implementation.md](features/multi-language-i18n-implementation.md) for the full checklist (config, translations, page wrappers, language switcher, build verification).

## Deployment

GitHub Actions builds on push to `main` and deploys to GitHub Pages (Node 22).
