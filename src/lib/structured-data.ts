import type { Locale } from '../i18n/types';
import type { Translations } from '../i18n/types';

export interface StructuredDataItem {
	name: string;
	description: string;
}

export interface StructuredDataStudy {
	name: string;
	description: string;
	url: string;
}

export interface StructuredDataFaqItem {
	question: string;
	answer: string;
}

export interface StructuredDataPricingTier {
	name: string;
	price: string;
	description: string;
	features: string[];
}

export interface HomeStructuredDataInput {
	siteUrl: string;
	pageUrl: string;
	title: string;
	description: string;
	socialImageUrl: string;
	appIconUrl: string;
	playStoreUrl: string;
	inLanguage: string;
	locale: Locale;
	features: StructuredDataItem[];
	benefits: StructuredDataItem[];
	howToSteps: StructuredDataItem[];
	includedMixCategories: string[];
	faqItems: StructuredDataFaqItem[];
	pricingTiers: StructuredDataPricingTier[];
	researchStudies: StructuredDataStudy[];
}

export interface PageStructuredDataInput {
	siteUrl: string;
	pageUrl: string;
	title: string;
	description: string;
	socialImageUrl: string;
	inLanguage: string;
}

const WEBSITE_FRAGMENT = '#website';
const ORGANIZATION_FRAGMENT = '#organization';
const APP_FRAGMENT = '#mindstate-app';

const PROFILE_URLS = [
	'https://play.google.com/store/apps/details?id=com.michielroos.mindstate',
	'https://www.instagram.com/mindstatesoundtherapy/',
];

const KNOWS_ABOUT = [
	'Binaural beats',
	'Brainwave entrainment',
	'Isochronic tones',
	'Sound therapy',
	'Focus',
	'Relaxation',
	'Sleep',
	'Meditation',
];

function slugify(value: string): string {
	return value
		.toLowerCase()
		.replace(/[^a-z0-9]+/g, '-')
		.replace(/(^-|-$)/g, '');
}

function websiteId(siteUrl: string): string {
	return `${siteUrl}${WEBSITE_FRAGMENT}`;
}

function organizationId(siteUrl: string): string {
	return `${siteUrl}${ORGANIZATION_FRAGMENT}`;
}

function appId(siteUrl: string): string {
	return `${siteUrl}${APP_FRAGMENT}`;
}

function featureId(siteUrl: string, name: string): string {
	return `${siteUrl}#feature-${slugify(name)}`;
}

function benefitId(siteUrl: string, name: string): string {
	return `${siteUrl}#benefit-${slugify(name)}`;
}

function pricingTierId(siteUrl: string, name: string): string {
	return `${siteUrl}#pricing-${slugify(name)}`;
}

function studyId(url: string): string {
	return `${url}#study`;
}

export function buildHomeStructuredData(input: HomeStructuredDataInput) {
	const website = websiteId(input.siteUrl);
	const organization = organizationId(input.siteUrl);
	const app = appId(input.siteUrl);

	const featureNodes = input.features.map((feature) => ({
		'@type': 'SoftwareFeature',
		'@id': featureId(input.siteUrl, feature.name),
		name: feature.name,
		description: feature.description,
	}));

	const benefitNodes = input.benefits.map((benefit) => ({
		'@type': 'Thing',
		'@id': benefitId(input.siteUrl, benefit.name),
		name: benefit.name,
		description: benefit.description,
	}));

	const pricingNodes = input.pricingTiers.map((tier) => ({
		'@type': 'Offer',
		'@id': pricingTierId(input.siteUrl, tier.name),
		name: tier.name,
		description: tier.description,
		price: tier.price,
		priceCurrency: 'USD',
		seller: { '@id': organization },
		itemOffered: { '@id': app },
	}));

	const studyNodes = input.researchStudies.map((study) => ({
		'@type': 'ScholarlyArticle',
		'@id': studyId(study.url),
		name: study.name,
		description: study.description,
		url: study.url,
	}));

	return {
		'@context': 'https://schema.org',
		'@graph': [
			{
				'@type': 'WebSite',
				'@id': website,
				url: input.siteUrl,
				name: 'MindState',
				alternateName: 'Binaural Beat Studio',
				description: input.description,
				inLanguage: input.inLanguage,
				publisher: { '@id': organization },
			},
			{
				'@type': 'WebPage',
				'@id': `${input.pageUrl}#webpage`,
				url: input.pageUrl,
				name: input.title,
				description: input.description,
				inLanguage: input.inLanguage,
				isPartOf: { '@id': website },
				about: { '@id': app },
				primaryImageOfPage: {
					'@type': 'ImageObject',
					url: input.socialImageUrl,
					width: 1200,
					height: 630,
				},
			},
			{
				'@type': 'Organization',
				'@id': organization,
				name: 'MindStateLab BV',
				alternateName: 'MindState',
				url: input.siteUrl,
				logo: input.appIconUrl,
				sameAs: PROFILE_URLS,
				knowsAbout: KNOWS_ABOUT,
			},
			{
				'@type': 'MobileApplication',
				'@id': app,
				name: 'MindState',
				alternateName: 'Binaural Beat Studio',
				description: input.description,
				url: input.siteUrl,
				image: input.appIconUrl,
				applicationCategory: 'HealthApplication',
				operatingSystem: 'Android',
				offers: {
					'@type': 'Offer',
					price: '0',
					priceCurrency: 'USD',
					url: input.playStoreUrl,
				},
				downloadUrl: input.playStoreUrl,
				publisher: { '@id': organization },
				featureList: input.features.map((feature) => feature.name),
			},
			{
				'@type': 'ItemList',
				'@id': `${input.siteUrl}#features`,
				name: 'MindState features',
				itemListElement: input.features.map((feature, index) => ({
					'@type': 'ListItem',
					position: index + 1,
					item: { '@id': featureId(input.siteUrl, feature.name) },
				})),
			},
			{
				'@type': 'ItemList',
				'@id': `${input.siteUrl}#benefits`,
				name: 'MindState benefits',
				itemListElement: input.benefits.map((benefit, index) => ({
					'@type': 'ListItem',
					position: index + 1,
					item: { '@id': benefitId(input.siteUrl, benefit.name) },
				})),
			},
			{
				'@type': 'HowTo',
				'@id': `${input.siteUrl}#how-it-works`,
				name: 'How MindState works',
				description: input.howToSteps.map((step) => step.description).join(' '),
				step: input.howToSteps.map((step, index) => ({
					'@type': 'HowToStep',
					position: index + 1,
					name: step.name,
					text: step.description,
				})),
			},
			{
				'@type': 'ItemList',
				'@id': `${input.siteUrl}#included-mixes`,
				name: 'Included mix categories',
				itemListElement: input.includedMixCategories.map((category, index) => ({
					'@type': 'ListItem',
					position: index + 1,
					name: category,
				})),
			},
			{
				'@type': 'FAQPage',
				'@id': `${input.siteUrl}#faq`,
				mainEntity: input.faqItems.map((item) => ({
					'@type': 'Question',
					name: item.question,
					acceptedAnswer: {
						'@type': 'Answer',
						text: item.answer,
					},
				})),
			},
			{
				'@type': 'OfferCatalog',
				'@id': `${input.siteUrl}#pricing`,
				name: 'MindState pricing',
				itemListElement: input.pricingTiers.map((tier, index) => ({
					'@type': 'ListItem',
					position: index + 1,
					item: { '@id': pricingTierId(input.siteUrl, tier.name) },
				})),
			},
			{
				'@type': 'ItemList',
				'@id': `${input.siteUrl}#research`,
				name: 'Research studies',
				itemListElement: input.researchStudies.map((study, index) => ({
					'@type': 'ListItem',
					position: index + 1,
					item: { '@id': studyId(study.url) },
				})),
			},
			...featureNodes,
			...benefitNodes,
			...pricingNodes,
			...studyNodes,
		],
	};
}

export function buildPageStructuredData(input: PageStructuredDataInput) {
	const website = websiteId(input.siteUrl);

	return {
		'@context': 'https://schema.org',
		'@graph': [
			{
				'@type': 'WebSite',
				'@id': website,
				url: input.siteUrl,
				name: 'MindState',
				alternateName: 'Binaural Beat Studio',
				description: input.description,
				inLanguage: input.inLanguage,
			},
			{
				'@type': 'WebPage',
				'@id': `${input.pageUrl}#webpage`,
				url: input.pageUrl,
				name: input.title,
				description: input.description,
				inLanguage: input.inLanguage,
				isPartOf: { '@id': website },
				primaryImageOfPage: {
					'@type': 'ImageObject',
					url: input.socialImageUrl,
					width: 1200,
					height: 630,
				},
			},
		],
	};
}

export function buildDefaultStructuredData(options: {
	siteUrl: string;
	description: string;
	socialImageUrl: string;
	inLanguage?: string;
}) {
	return {
		'@context': 'https://schema.org',
		'@type': 'WebSite',
		name: 'MindState',
		alternateName: 'Binaural Beat Studio',
		url: options.siteUrl,
		description: options.description,
		inLanguage: options.inLanguage ?? 'en-US',
		image: options.socialImageUrl,
	};
}

function tierFeatures(translations: Translations, tier: 'free' | 'starter' | 'samplePacks'): string[] {
	const block = translations.pricing[tier];
	return (['feature1', 'feature2', 'feature3', 'feature4'] as const)
		.map((key) => block[key])
		.filter((value): value is string => typeof value === 'string' && value.trim().length > 0);
}

export function buildHomeStructuredDataFromTranslations(options: {
	siteUrl: string;
	pageUrl: string;
	title: string;
	description: string;
	socialImageUrl: string;
	appIconUrl: string;
	playStoreUrl: string;
	inLanguage: string;
	locale: Locale;
	translations: Translations;
	showIosFaq?: boolean;
}) {
	const { translations, showIosFaq = false } = options;
	const faqNumbers = showIosFaq ? ([1, 2, 3, 4, 5] as const) : ([1, 2, 3, 5] as const);

	return buildHomeStructuredData({
		siteUrl: options.siteUrl,
		pageUrl: options.pageUrl,
		title: options.title,
		description: options.description,
		socialImageUrl: options.socialImageUrl,
		appIconUrl: options.appIconUrl,
		playStoreUrl: options.playStoreUrl,
		inLanguage: options.inLanguage,
		locale: options.locale,
		features: ([1, 2, 3, 4, 5, 6] as const).map((n) => ({
			name: translations.features[`feature${n}`].title,
			description: translations.features[`feature${n}`].description,
		})),
		benefits: ([1, 2, 3, 4, 5, 6] as const).map((n) => ({
			name: translations.aboutBinauralBeats.benefits[`benefit${n}`].title,
			description: translations.aboutBinauralBeats.benefits[`benefit${n}`].description,
		})),
		howToSteps: ([1, 2, 3, 4, 5] as const).map((n) => ({
			name: translations.howItWorks[`step${n}`].title,
			description: translations.howItWorks[`step${n}`].description,
		})),
		includedMixCategories: ([1, 2, 3, 4, 5, 6, 7, 8] as const).map((n) =>
			translations.includedMixes[`category${n}`]
		),
		faqItems: faqNumbers.map((n) => ({
			question: translations.faq[`q${n}`],
			answer: translations.faq[`a${n}`],
		})),
		pricingTiers: (['free', 'starter', 'samplePacks'] as const).map((tier) => ({
			name: translations.pricing[tier].name,
			price: translations.pricing[tier].price,
			description: translations.pricing[tier].description,
			features: tierFeatures(translations, tier),
		})),
		researchStudies: (
			['adhdNoise', 'adhdBinaural', 'metaAnalysis', 'anxiety', 'memory', 'tinnitus'] as const
		).map((key) => ({
			name: translations.aboutBinauralBeats.research.studies[key].title,
			description: translations.aboutBinauralBeats.research.studies[key].description,
			url: translations.aboutBinauralBeats.research.studies[key].url,
		})),
	});
}
