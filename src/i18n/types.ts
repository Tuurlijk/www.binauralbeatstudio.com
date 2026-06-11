export type Locale = 'en' | 'ar' | 'es' | 'hi' | 'id' | 'ja' | 'nl' | 'pt' | 'ru' | 'zh';

interface PricingTier {
  name: string;
  price: string;
  description: string;
  feature1: string;
  feature2: string;
  feature3?: string;
  feature4?: string;
}

export interface Translations {
  meta: {
    title: string;
    description: string;
  };
  nav: {
    features: string;
    howItWorks: string;
    screenshots: string;
    about: string;
    benefits: string;
    download: string;
    downloadApp: string;
    appExamples: string;
    research: string;
    more: string;
    pricing: string;
    faq: string;
  };
  hero: {
    headline: string;
    subtitle: string;
    tagline: string;
    ctaDownload: string;
    ctaLearnMore: string;
  };
  store: {
    playStore: string;
  };
  features: {
    titlePrefix: string;
    titleHighlight: string;
    titleSuffix: string;
    pitch: string;
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
    seeMore: string;
    allPageTitle: string;
    allPageDescription: string;
    lightMode: string;
    darkMode: string;
    backHome: string;
    player: string;
    mixes: string;
    beatPicker: string;
    quickEditor: string;
    shareQr: string;
    addTrack: string;
    fullEditor: string;
    ritualsList: string;
    ritualEdit: string;
  };
  includedMixes: {
    title: string;
    subtitle: string;
    category1: string;
    category2: string;
    category3: string;
    category4: string;
    category5: string;
    category6: string;
    category7: string;
    category8: string;
    note: string;
  };
  rituals: {
    title: string;
    subtitle: string;
    bullet1: string;
    bullet2: string;
    bullet3: string;
    bullet4: string;
  };
  pricing: {
    title: string;
    subtitle: string;
    free: PricingTier;
    starter: PricingTier;
    samplePacks: PricingTier;
  };
  faq: {
    title: string;
    q1: string;
    a1: string;
    q2: string;
    a2: string;
    q3: string;
    a3: string;
    q4: string;
    a4: string;
    q5: string;
    a5: string;
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
      explore: string;
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
      frequencyIntro: string;
      frequencyDelta: string;
      frequencyTheta: string;
      frequencyAlpha: string;
      frequencyBeta: string;
      frequencyGamma: string;
      personalization: string;
    };
    adhdNoise: {
      title: string;
      subtitle: string;
      description: string;
    };
    adhdBinaural: {
      title: string;
      subtitle: string;
      description: string;
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
        adhdNoise: { title: string; description: string; url: string };
        adhdBinaural: { title: string; description: string; url: string };
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
    quote9: { text: string; source: string };
    quote10: { text: string; source: string };
  };
}

