export type Locale = 'en' | 'ar' | 'es' | 'hi' | 'id' | 'nl' | 'pt' | 'ru' | 'zh';

export interface Translations {
  meta: {
    title: string;
    description: string;
  };
  nav: {
    features: string;
    howItWorks: string;
    screenshots: string;
    download: string;
  };
  hero: {
    title: string;
    titleHighlight: string;
    titleSuffix: string;
    subtitle: string;
    ctaDownload: string;
    ctaLearnMore: string;
    tagline: string;
  };
  features: {
    title: string;
    subtitle: string;
    feature1: { title: string; description: string };
    feature2: { title: string; description: string };
    feature3: { title: string; description: string };
    feature4: { title: string; description: string };
    feature5: { title: string; description: string };
    feature6: { title: string; description: string };
  };
  howItWorks: {
    title: string;
    subtitle: string;
    step1: { title: string; description: string };
    step2: { title: string; description: string };
    step3: { title: string; description: string };
    step4: { title: string; description: string };
    step5: { title: string; description: string };
  };
  screenshots: {
    title: string;
    subtitle: string;
    sessionBrowser: string;
    sessionEditor: string;
    trackTypePicker: string;
    mainPlayer: string;
    pointEditor: string;
    qrSharing: string;
  };
  cta: {
    title: string;
    subtitle: string;
    ctaDownload: string;
    ctaViewFeatures: string;
    benefit1: { title: string; description: string };
    benefit2: { title: string; description: string };
    benefit3: { title: string; description: string };
  };
  aboutBinauralBeats: {
    heroTitle: string;
    heroSubtitle: string;
    benefits: {
      title: string;
      subtitle: string;
      benefit1: { title: string; description: string };
      benefit2: { title: string; description: string };
      benefit3: { title: string; description: string };
      benefit4: { title: string; description: string };
      benefit5: { title: string; description: string };
      benefit6: { title: string; description: string };
    };
    howItWorks: {
      title: string;
      subtitle: string;
      explanation: string;
      noHeadphones: string;
      personalization: string;
    };
    safety: {
      title: string;
      subtitle: string;
      general: string;
      precautions: string;
    };
    research: {
      title: string;
      subtitle: string;
      findings: string;
      studies: {
        metaAnalysis: { title: string; description: string; url: string };
        anxiety: { title: string; description: string; url: string };
        memory: { title: string; description: string; url: string };
        tinnitus: { title: string; description: string; url: string };
      };
    };
  };
  footer: {
    description: string;
    links: string;
    download: string;
    downloadDescription: string;
    copyright: string;
  };
  languageSwitcher: {
    label: string;
    current: string;
    switchTo: string;
  };
  quotes: {
    title: string;
    subtitle: string;
    quote1: { text: string; source: string };
    quote2: { text: string; source: string };
    quote3: { text: string; source: string };
    quote4: { text: string; source: string };
    quote5: { text: string; source: string };
    quote6: { text: string; source: string };
    quote7: { text: string; source: string };
    quote8: { text: string; source: string };
  };
}

