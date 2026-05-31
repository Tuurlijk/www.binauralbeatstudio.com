#!/usr/bin/env python3
"""Apply v2.1.5 brief translations to locale JSON files (deep merge)."""

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src" / "i18n"


def deep_merge(base: dict, overlay: dict) -> dict:
    result = deepcopy(base)
    for key, value in overlay.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result


OVERLAYS: dict[str, dict] = {
    "es": {
        "meta": {
            "title": "MindState: Beats y ruido personalizados",
            "description": "Diseña mezclas de sonido multicapa con beats binaurales, monaurales e isocrónicos, ruido, efectos ambientales y clips de audio. 33 mezclas incluidas, editores Quick y Full, compartir QR y Daily Rituals.",
        },
        "nav": {"pricing": "Precios", "faq": "Preguntas frecuentes"},
        "hero": {
            "subtitle": "Beats y ruido personalizados para relajarte, concentrarte, meditar, ser creativo y dormir mejor. Si buscas alivio de síntomas de TDAH, meditación más profunda, mejor sueño, más creatividad o mayor enfoque, MindState te da herramientas para diseñar mezclas a tu medida.",
            "tagline": "Disponible en Android con calidad de audio profesional. Gratis para probar.",
        },
        "store": {"playStore": "Disponible en Google Play"},
        "features": {
            "titlePrefix": "Crea mezclas",
            "titleHighlight": "multicapa",
            "titleSuffix": "personalizadas",
            "pitch": "A diferencia de apps de bienestar solo con presets, MindState te da control profesional sobre cada capa, frecuencia y envolvente de volumen, o empieza con 33 mezclas incluidas en nueve categorías. Comparte mezclas por QR, programa Daily Rituals y escucha con controles en pantalla de bloqueo y audio nativo con motor de síntesis Rust.",
            "title": "Funciones principales",
            "subtitle": "Herramientas profesionales para enfoque, relajación, sueño, meditación y creatividad.",
            "feature1": {"title": "Editor Quick y editor Full", "description": "Editor Quick: hasta cuatro ranuras de tono, ruido, efecto o archivo con vista previa en vivo y selector de beats. Editor Full: pistas ilimitadas, envolventes de volumen, automatización de ruido y tipos de pista categorizados. Cambia de editor sin perder tu trabajo."},
            "feature2": {"title": "Mezcla multicapa", "description": "Combina beats binaurales, monaurales e isocrónicos; ruido blanco, rosa, marrón, verde y coloreado; efectos ambientales (lluvia, océano, viento, ventilador, cascada, disco antiguo); y clips MP3, WAV o FLAC temporizados, cada uno con volumen independiente."},
            "feature3": {"title": "33 mezclas incluidas", "description": "Mezclas curadas en Sueño, Enfoque, Meditación, Relajación, Creatividad, Estado de ánimo, Estudio y Relaxed kid. 17 gratis; 16 extendidas con suscripción Starter. Duplica cualquier mezcla incluida para personalizarla."},
            "feature4": {"title": "Código QR y enlace para compartir", "description": "Codifica mezclas como URLs mindstate://. Escanea, previsualiza, edita y guarda. QR con logo sobre fondo blanco. Los enlaces solo incluyen la estructura de la mezcla (no arte personalizado ni archivos de audio importados)."},
            "feature5": {"title": "Daily Rituals", "description": "Programa una mezcla por hora y días de repetición. Crea un ritual desde la barra del reproductor o la pantalla Rituals. Abre el reproductor con transporte en pantalla de bloqueo cuando toque escuchar."},
            "feature6": {"title": "Audio nativo profesional", "description": "Síntesis Rust en tiempo real con tonos de fase continua, transiciones suaves y fundido anti-clic. Reproducción, pausa y búsqueda en pantalla de bloqueo, Smart Pause con auriculares y arte por categoría."},
        },
        "howItWorks": {
            "subtitle": "Explora, crea, ajusta, guarda y escucha en cinco pasos",
            "step1": {"title": "Explorar o crear", "description": "Empieza con mezclas incluidas o un editor Quick o Full en blanco."},
            "step2": {"title": "Añadir capas", "description": "Añade tonos, ruido, efectos ambientales o tus archivos de audio. Elige tipos con chips ilustrados en la hoja de añadir pista del editor Full."},
            "step3": {"title": "Ajustar", "description": "Configura frecuencias portadora y de beat, portadores Solfeggio y volúmenes. Modela envolventes y automatización de ruido en el editor Full."},
            "step4": {"title": "Previsualizar y guardar", "description": "Vista previa en vivo mientras editas. Guarda mezclas personalizadas en Mis mezclas con suscripción Starter."},
            "step5": {"title": "Escuchar, compartir, programar", "description": "Reproduce con controles en pantalla de bloqueo, comparte por QR o enlace y programa opcionalmente un Daily Ritual."},
        },
        "screenshots": {
            "subtitle": "Interfaz Material 3 con modo claro y oscuro. App disponible en 7 idiomas.",
            "player": "Escucha con controles en pantalla de bloqueo", "mixes": "Explora mezclas incluidas y personalizadas",
            "beatPicker": "Elige bandas de ondas cerebrales y tonos Solfeggio", "quickEditor": "Crea una mezcla en cuatro ranuras",
            "shareQr": "Comparte mezclas por QR o enlace", "addTrack": "Añade tonos, ruido, efectos y archivos",
            "fullEditor": "Control total de cada pista", "ritualsList": "Programa Daily Rituals", "ritualEdit": "Hora, días de repetición y mezcla",
        },
        "cta": {
            "subtitle": "Empieza con 17 mezclas incluidas gratis, o desbloquea Starter para guardar mezclas ilimitadas y reproducir contenido extendido.",
            "benefit1": {"title": "✓ 17 mezclas gratis", "description": "Reproduce mezclas incluidas, importa por QR y duplica para personalizar"},
            "benefit2": {"title": "✓ Suscripción Starter", "description": "Guarda mezclas personalizadas ilimitadas y reproduce 16 mezclas extendidas"},
            "benefit3": {"title": "✓ Audio profesional", "description": "Motor de síntesis Rust con controles en pantalla de bloqueo"},
        },
        "footer": {"description": "Beats y ruido personalizados para enfoque, relajación, sueño, meditación y creatividad.", "downloadDescription": "Disponible en Google Play. iOS próximamente."},
        "pricing": {
            "title": "Precios", "subtitle": "Empieza gratis; mejora cuando quieras guardar mezclas personalizadas y reproducir contenido extendido.",
            "free": {"name": "Gratis", "price": "$0", "description": "Explora MindState sin coste inicial.", "feature1": "Reproduce 17 mezclas incluidas", "feature2": "Explora e importa mezclas por QR", "feature3": "Duplica mezclas incluidas y edita con vista previa", "feature4": "Onboarding y contenido informativo"},
            "starter": {"name": "Starter", "price": "Mensual o anual", "description": "Acceso completo con prueba gratuita gestionada por la tienda.", "feature1": "Guarda mezclas personalizadas ilimitadas", "feature2": "Reproduce 16 mezclas incluidas extendidas", "feature3": "Crea Daily Rituals desde el reproductor", "feature4": "Planes mensuales y anuales en Google Play"},
            "samplePacks": {"name": "Paquetes de muestras", "price": "Compra única", "description": "Paquetes de audio opcionales para pistas de archivo extra.", "feature1": "Ejemplo: Chakra Bar Chimes (7 tonos)", "feature2": "Añade pistas MP3 al editor Full"},
        },
        "includedMixes": {
            "title": "33 mezclas incluidas", "subtitle": "Puntos de partida curados en nueve categorías. Duplica cualquier mezcla para hacerla tuya.",
            "category1": "Sueño", "category2": "Enfoque", "category3": "Meditación", "category4": "Relajación",
            "category5": "Creatividad", "category6": "Estado de ánimo", "category7": "Estudio", "category8": "Relaxed kid",
            "note": "17 mezclas son gratis. 16 extendidas requieren suscripción Starter.",
        },
        "rituals": {
            "title": "Daily Rituals", "subtitle": "Programa una mezcla por hora y días de repetición para que encaje en tu rutina.",
            "bullet1": "Crea un ritual desde la pantalla Rituals o la barra del reproductor con suscripción.",
            "bullet2": "Elige hora, días de repetición y qué mezcla reproducir.",
            "bullet3": "Android usa programación fiable de alarmas con guía opcional de No molestar.",
            "bullet4": "iOS usa notificaciones locales. Los rituales se reprograman al cambiar de zona horaria.",
        },
        "faq": {
            "title": "Preguntas frecuentes",
            "q1": "¿Qué archivos de audio puedo importar?", "a1": "MP3, WAV y FLAC desde el almacenamiento del dispositivo o recursos incluidos y de paquetes de muestras.",
            "q2": "¿Los códigos QR incluyen mi audio personalizado?", "a2": "No. QR y enlaces solo incluyen la estructura de la mezcla (tonos, ruido, efectos). Vuelve a adjuntar pistas de archivo tras importar.",
            "q3": "¿Cómo funcionan Daily Rituals en Android?", "a3": "Alarmas y notificaciones. Concede permisos de alarma exacta, batería y notificaciones cuando se soliciten. El acceso opcional a No molestar permite reproducir durante DND.",
            "q4": "¿Cómo funcionan Daily Rituals en iOS?", "a4": "Notificaciones locales. Toca la alerta para abrir MindState y reproducir la mezcla programada.",
            "q5": "¿Puedo crear un ritual desde una mezcla que estoy reproduciendo?", "a5": "Sí. Usa Crear ritual en la barra del reproductor con suscripción.",
        },
        "aboutBinauralBeats": {"benefits": {"subtitle": "Los beats binaurales, tonos isocrónicos, portadores Solfeggio y capas de ruido pueden apoyar el enfoque, la relajación, el sueño, la meditación, la creatividad y el estado de ánimo."}},
    },
    "ar": {
        "meta": {"title": "MindState: نغمات وضوضاء مخصصة", "description": "صمّم مزيجات صوت متعددة الطبقات مع نغمات ثنائية و أحادية ومتساوية الإيقاع، وضوضاء، ومؤثرات محيطة، ومقاطع صوت. 33 مزيجاً مضمناً، محرر Quick و Full، مشاركة QR و Daily Rituals."},
        "nav": {"pricing": "الأسعار", "faq": "الأسئلة الشائعة"},
        "hero": {"subtitle": "نغمات وضوضاء مخصصة للاسترخاء والتركيز والتأمل والإبداع ونوم أفضل. إن كنت تبحث عن تخفيف أعراض AD/HD، أو تأمل أعمق، أو نوم أفضل، أو إبداع أقوى، أو تركيز أوضح، يمنحك MindState أدوات لتصميم مزيجات تناسب احتياجاتك.", "tagline": "متوفر على Android بجودة صوت احترافية. مجاني للتجربة."},
        "store": {"playStore": "احصل عليه من Google Play"},
        "features": {
            "titlePrefix": "أنشئ مزيجات", "titleHighlight": "متعددة الطبقات", "titleSuffix": "مخصصة",
            "pitch": "على عكس تطبيقات العافية ذات الإعدادات المسبقة فقط، يمنحك MindState تحكماً احترافياً في كل طبقة وتردد ومغلف حجم، أو ابدأ من 33 مزيجاً مضمناً في تسع فئات. شارك المزيجات عبر QR، وجدول Daily Rituals، واستمع بضوابط شاشة القفل وجودة صوت أصلية بمحرك تركيب Rust.",
            "title": "أهم الميزات", "subtitle": "أدوات احترافية للتركيز والاسترخاء والنوم والتأمل والإبداع.",
            "feature1": {"title": "محرر Quick ومحرر Full", "description": "محرر Quick: حتى أربع فتحات لنغمة أو ضوضاء أو مؤثر أو ملف مع معاينة مباشرة ومُنتقي نغمات. محرر Full: مسارات غير محدودة، مغلفات حجم، أتمتة ضوضاء، وأنواع إضافة مسار مصنفة. بدّل بين المحررين دون فقدان العمل."},
            "feature2": {"title": "مزج متعدد الطبقات", "description": "اجمع نغمات ثنائية وأحادية ومتساوية الإيقاع؛ ضوضاء بيضاء ووردية وبنية وخضراء وملونة؛ مؤثرات محيطة (مطر، محيط، رياح، مروحة، شلال، أسطوانة قديمة)؛ ومقاطع MP3 وWAV وFLAC مؤقتة، لكل منها حجم مستقل."},
            "feature3": {"title": "33 مزيجاً مضمناً", "description": "مزيجات منتقاة في النوم والتركيز والتأمل والاسترخاء والإبداع والمزاج والدراسة و Relaxed kid. 17 مجاناً؛ 16 ممتدة باشتراك Starter. انسخ أي مزيج مضمّن للتخصيص."},
            "feature4": {"title": "رمز QR ومشاركة الرابط", "description": "شفّر المزيجات كعناوين mindstate://. امسح وعاين وحرّر واحفظ. QR بعلامة على خلفية بيضاء. الروابط تحمل هيكل المزيج فقط (لا فن مخصص ولا ملفات صوت مستوردة)."},
            "feature5": {"title": "Daily Rituals", "description": "جدول مزيجاً بالوقت وأيام التكرار. أنشئ طقساً من شريط المشغّل أو شاشة Rituals. يفتح المشغّل الرئيسي مع تحكم شاشة القفل عند وقت الاستماع."},
            "feature6": {"title": "صوت أصلي احترافي", "description": "تركيب Rust في الوقت الفعلي بنغمات متصلة الطور، انزلاقات سلسة، وتلاشٍ مضاد للنقرات. تشغيل وإيقاف وبحث على شاشة القفل، Smart Pause مع السماعات، وفن مزيج حسب الفئة."},
        },
        "howItWorks": {
            "subtitle": "تصفح، ابنِ، ضبط، احفظ، واستمع في خمس خطوات",
            "step1": {"title": "تصفح أو أنشئ", "description": "ابدأ من مزيجات مضمّنة أو محرر Quick أو Full فارغ."},
            "step2": {"title": "أضف طبقات", "description": "أضف نغمات وضوضاء ومؤثرات محيطة أو ملفاتك. اختر الأنواع من رقائق مصورة في ورقة إضافة المسار في محرر Full."},
            "step3": {"title": "ضبط", "description": "اضبط ترددات الحامل والنبض، حاملات Solfeggio، والأحجام. شكّل المغلفات وأتمتة الضوضاء في محرر Full."},
            "step4": {"title": "معاينة وحفظ", "description": "معاينة مباشرة أثناء التحرير. احفظ المزيجات المخصصة في مزيجاتي باشتراك Starter."},
            "step5": {"title": "استمع، شارك، جدول", "description": "شغّل بضوابط شاشة القفل، شارك عبر QR أو رابط، وجدول Daily Ritual اختيارياً."},
        },
        "screenshots": {
            "subtitle": "واجهة Material 3 بالوضعين الفاتح والداكن. التطبيق بسبع لغات.",
            "player": "استمع بضوابط شاشة القفل", "mixes": "تصفح المزيجات المضمّنة والمخصصة",
            "beatPicker": "اختر نطاقات موجات الدماغ ونغمات Solfeggio", "quickEditor": "ابنِ مزيجاً في أربع فتحات",
            "shareQr": "شارك المزيجات عبر QR أو رابط", "addTrack": "أضف نغمات وضوضاء ومؤثرات وملفات",
            "fullEditor": "تحكم كامل بكل مسار", "ritualsList": "جدول Daily Rituals", "ritualEdit": "الوقت وأيام التكرار والمزيج",
        },
        "cta": {
            "subtitle": "ابدأ بـ 17 مزيجاً مضمناً مجاناً، أو فعّل Starter لحفظ مزيجات مخصصة غير محدودة وتشغيل محتوى ممتد.",
            "benefit1": {"title": "✓ 17 مزيجاً مجاناً", "description": "شغّل المزيجات المضمّنة، استورد عبر QR، وانسخ للتخصيص"},
            "benefit2": {"title": "✓ اشتراك Starter", "description": "احفظ مزيجات مخصصة غير محدودة وشغّل 16 مزيجاً مضمناً ممتداً"},
            "benefit3": {"title": "✓ صوت احترافي", "description": "محرك تركيب Rust مع ضوابط شاشة القفل"},
        },
        "footer": {"description": "نغمات وضوضاء مخصصة للتركيز والاسترخاء والنوم والتأمل والإبداع.", "downloadDescription": "متوفر على Google Play. iOS قريباً."},
        "pricing": {
            "title": "الأسعار", "subtitle": "ابدأ مجاناً، وطوّر عندما تريد حفظ مزيجات مخصصة وتشغيل محتوى مضمّن ممتد.",
            "free": {"name": "مجاني", "price": "$0", "description": "استكشف MindState دون تكلفة مقدمة.", "feature1": "شغّل 17 مزيجاً مضمناً", "feature2": "تصفح واستورد المزيجات عبر QR", "feature3": "انسخ المزيجات المضمّنة وحرّر بمعاينة", "feature4": "التهيئة ومحتوى حول التطبيق"},
            "starter": {"name": "Starter", "price": "شهري أو سنوي", "description": "وصول كامل مع تجربة مجانية من المتجر.", "feature1": "احفظ مزيجات مخصصة غير محدودة", "feature2": "شغّل 16 مزيجاً مضمناً ممتداً", "feature3": "أنشئ Daily Rituals من المشغّل", "feature4": "خطط شهرية وسنوية عبر Google Play"},
            "samplePacks": {"name": "حزم عينات", "price": "شراء لمرة واحدة", "description": "حزم صوت اختيارية لأصوات مسارات ملف إضافية.", "feature1": "مثال: Chakra Bar Chimes (7 نغمات)", "feature2": "يضيف مسارات MP3 إلى محرر Full"},
        },
        "includedMixes": {
            "title": "33 مزيجاً مضمناً", "subtitle": "نقاط بداية منتقاة في تسع فئات. انسخ أي مزيج لتجعله ملكك.",
            "category1": "النوم", "category2": "التركيز", "category3": "التأمل", "category4": "الاسترخاء",
            "category5": "الإبداع", "category6": "المزاج", "category7": "الدراسة", "category8": "Relaxed kid",
            "note": "17 مزيجاً مجانياً للتشغيل. 16 ممتدة تتطلب اشتراك Starter.",
        },
        "rituals": {
            "title": "Daily Rituals", "subtitle": "جدول مزيجاً بالوقت وأيام التكرار ليناسب روتينك.",
            "bullet1": "أنشئ طقساً من شاشة Rituals أو شريط المشغّل عند الاشتراك.",
            "bullet2": "اختر الوقت وأيام التكرار وأي مزيج يُشغّل.",
            "bullet3": "Android يستخدم جدولة منبهات موثوقة مع إرشاد اختياري لوضع عدم الإزعاج.",
            "bullet4": "iOS يستخدم إشعارات محلية. تُعاد جدولة الطقوس عند تغيير المناطق الزمنية.",
        },
        "faq": {
            "title": "الأسئلة الشائعة",
            "q1": "ما ملفات الصوت التي يمكن استيرادها؟", "a1": "MP3 وWAV وFLAC من تخزين الجهاز أو أصول مضمّنة وحزم عينات.",
            "q2": "هل تتضمن رموز QR صوتي المخصص؟", "a2": "لا. QR والروابط تتضمن هيكل المزيج (نغمات، ضوضاء، مؤثرات) فقط. أعد إرفاق مسارات الملف بعد الاستيراد.",
            "q3": "كيف تعمل Daily Rituals على Android؟", "a3": "منبهات وإشعارات. امنح أذونات المنبه الدقيق والبطارية والإشعارات عند الطلب. الوصول الاختياري لعدم الإزعاج يتيح التشغيل أثناء DND.",
            "q4": "كيف تعمل Daily Rituals على iOS؟", "a4": "إشعارات محلية. اضغط التنبيه لفتح MindState وتشغيل المزيج المجدول.",
            "q5": "هل يمكن إنشاء طقس من مزيج أستمع إليه؟", "a5": "نعم. استخدم إنشاء طقس في شريط المشغّل عند الاشتراك.",
        },
        "aboutBinauralBeats": {"benefits": {"subtitle": "النغمات الثنائية والنغمات المتساوية الإيقاع وحاملات Solfeggio وطبقات الضوضاء قد تدعم التركيز والاسترخاء والنوم والتأمل والإبداع والمزاج."}},
    },
    "pt": {
        "meta": {"title": "MindState: Beats e ruído personalizados", "description": "Crie mixes de som multicamadas com beats binaurais, monaurais e isocrônicos, ruído, efeitos ambientes e clipes de áudio. 33 mixes incluídos, editores Quick e Full, compartilhamento QR e Daily Rituals."},
        "nav": {"pricing": "Preços", "faq": "Perguntas frequentes"},
        "hero": {"subtitle": "Beats e ruído personalizados para relaxar, focar, meditar, ser criativo e dormir melhor. Se você busca alívio de sintomas de TDAH, meditação mais profunda, sono melhor, mais criatividade ou foco mais nítido, o MindState oferece ferramentas para criar mixes sob medida.", "tagline": "Disponível no Android com qualidade de áudio profissional. Grátis para experimentar."},
        "store": {"playStore": "Disponível no Google Play"},
        "features": {
            "titlePrefix": "Crie mixes", "titleHighlight": "multicamadas", "titleSuffix": "personalizados",
            "pitch": "Diferente de apps de bem-estar só com presets, o MindState dá controle profissional sobre cada camada, frequência e envelope de volume, ou comece com 33 mixes incluídos em nove categorias. Compartilhe mixes por QR, agende Daily Rituals e ouça com controles na tela de bloqueio e áudio nativo com motor de síntese Rust.",
            "title": "Principais recursos", "subtitle": "Ferramentas profissionais para foco, relaxamento, sono, meditação e criatividade.",
            "feature1": {"title": "Editor Quick e editor Full", "description": "Editor Quick: até quatro slots de tom, ruído, efeito ou arquivo com prévia ao vivo e seletor de beats. Editor Full: faixas ilimitadas, envelopes de volume, automação de ruído e tipos de faixa categorizados. Troque de editor sem perder o trabalho."},
            "feature2": {"title": "Mixagem multicamada", "description": "Combine beats binaurais, monaurais e isocrônicos; ruído branco, rosa, marrom, verde e colorido; efeitos ambientes (chuva, oceano, vento, ventilador, cachoeira, disco antigo); e clipes MP3, WAV ou FLAC temporizados, cada um com volume independente."},
            "feature3": {"title": "33 mixes incluídos", "description": "Mixes curados em Sono, Foco, Meditação, Relaxamento, Criatividade, Humor, Estudo e Relaxed kid. 17 grátis; 16 estendidos com assinatura Starter. Duplique qualquer mix incluído para personalizar."},
            "feature4": {"title": "QR Code e link para compartilhar", "description": "Codifique mixes como URLs mindstate://. Escaneie, pré-visualize, edite e salve. QR com logo em fundo branco. Links levam só a estrutura do mix (sem arte personalizada nem arquivos importados)."},
            "feature5": {"title": "Daily Rituals", "description": "Agende um mix por horário e dias de repetição. Crie um ritual na barra do player ou na tela Rituals. Abre o player principal com transporte na tela de bloqueio na hora de ouvir."},
            "feature6": {"title": "Áudio nativo profissional", "description": "Síntese Rust em tempo real com tons de fase contínua, transições suaves e fade anti-clique. Play, pause e seek na tela de bloqueio, Smart Pause com fones e arte por categoria."},
        },
        "howItWorks": {
            "subtitle": "Navegue, crie, ajuste, salve e ouça em cinco passos",
            "step1": {"title": "Navegar ou criar", "description": "Comece com mixes incluídos ou um editor Quick ou Full em branco."},
            "step2": {"title": "Adicionar camadas", "description": "Adicione tons, ruído, efeitos ambientes ou seus arquivos. Escolha tipos nos chips ilustrados na folha de adicionar faixa do editor Full."},
            "step3": {"title": "Ajustar", "description": "Defina frequências de portadora e beat, portadoras Solfeggio e volumes. Modele envelopes e automação de ruído no editor Full."},
            "step4": {"title": "Pré-visualizar e salvar", "description": "Prévia ao vivo enquanto edita. Salve mixes personalizados em Meus mixes com assinatura Starter."},
            "step5": {"title": "Ouvir, compartilhar, agendar", "description": "Toque com controles na tela de bloqueio, compartilhe por QR ou link e agende opcionalmente um Daily Ritual."},
        },
        "screenshots": {
            "subtitle": "Interface Material 3 com modo claro e escuro. App em 7 idiomas.",
            "player": "Ouça com controles na tela de bloqueio", "mixes": "Navegue mixes incluídos e personalizados",
            "beatPicker": "Escolha bandas de ondas cerebrais e tons Solfeggio", "quickEditor": "Monte um mix em quatro slots",
            "shareQr": "Compartilhe mixes por QR ou link", "addTrack": "Adicione tons, ruído, efeitos e arquivos",
            "fullEditor": "Controle total de cada faixa", "ritualsList": "Agende Daily Rituals", "ritualEdit": "Horário, dias de repetição e mix",
        },
        "cta": {
            "subtitle": "Comece com 17 mixes incluídos grátis, ou desbloqueie Starter para salvar mixes ilimitados e tocar conteúdo estendido.",
            "benefit1": {"title": "✓ 17 mixes grátis", "description": "Toque mixes incluídos, importe por QR e duplique para personalizar"},
            "benefit2": {"title": "✓ Assinatura Starter", "description": "Salve mixes personalizados ilimitados e toque 16 mixes incluídos estendidos"},
            "benefit3": {"title": "✓ Áudio profissional", "description": "Motor de síntese Rust com controles na tela de bloqueio"},
        },
        "footer": {"description": "Beats e ruído personalizados para foco, relaxamento, sono, meditação e criatividade.", "downloadDescription": "Disponível no Google Play. iOS em breve."},
        "pricing": {
            "title": "Preços", "subtitle": "Comece grátis; faça upgrade quando quiser salvar mixes personalizados e tocar conteúdo incluído estendido.",
            "free": {"name": "Grátis", "price": "R$ 0", "description": "Explore o MindState sem custo inicial.", "feature1": "Toque 17 mixes incluídos", "feature2": "Navegue e importe mixes por QR", "feature3": "Duplique mixes incluídos e edite com prévia", "feature4": "Onboarding e conteúdo sobre o app"},
            "starter": {"name": "Starter", "price": "Mensal ou anual", "description": "Acesso completo com teste grátis gerenciado pela loja.", "feature1": "Salve mixes personalizados ilimitados", "feature2": "Toque 16 mixes incluídos estendidos", "feature3": "Crie Daily Rituals no player", "feature4": "Planos mensais e anuais via Google Play"},
            "samplePacks": {"name": "Pacotes de amostras", "price": "Compra única", "description": "Pacotes de áudio opcionais para sons extras em faixas de arquivo.", "feature1": "Exemplo: Chakra Bar Chimes (7 tons)", "feature2": "Adiciona faixas MP3 ao editor Full"},
        },
        "includedMixes": {
            "title": "33 mixes incluídos", "subtitle": "Pontos de partida curados em nove categorias. Duplique qualquer mix para torná-lo seu.",
            "category1": "Sono", "category2": "Foco", "category3": "Meditação", "category4": "Relaxamento",
            "category5": "Criatividade", "category6": "Humor", "category7": "Estudo", "category8": "Relaxed kid",
            "note": "17 mixes são grátis para tocar. 16 estendidos exigem assinatura Starter.",
        },
        "rituals": {
            "title": "Daily Rituals", "subtitle": "Agende um mix por horário e dias de repetição para encaixar na sua rotina.",
            "bullet1": "Crie um ritual na tela Rituals ou na barra do player com assinatura.",
            "bullet2": "Escolha horário, dias de repetição e qual mix tocar.",
            "bullet3": "Android usa agendamento confiável de alarmes com orientação opcional de Não perturbe.",
            "bullet4": "iOS usa notificações locais. Rituais são reagendados ao mudar de fuso horário.",
        },
        "faq": {
            "title": "Perguntas frequentes",
            "q1": "Quais arquivos de áudio posso importar?", "a1": "MP3, WAV e FLAC do armazenamento do dispositivo ou ativos incluídos e de pacotes de amostras.",
            "q2": "Os QR codes incluem meu áudio personalizado?", "a2": "Não. QR e links incluem só a estrutura do mix (tons, ruído, efeitos). Reanexe faixas de arquivo após importar.",
            "q3": "Como funcionam Daily Rituals no Android?", "a3": "Alarmes e notificações. Conceda permissões de alarme exato, bateria e notificações quando solicitado. Acesso opcional a Não perturbe permite tocar durante DND.",
            "q4": "Como funcionam Daily Rituals no iOS?", "a4": "Notificações locais. Toque no alerta para abrir o MindState e tocar o mix agendado.",
            "q5": "Posso criar um ritual de um mix que estou tocando?", "a5": "Sim. Use Criar ritual na barra do player com assinatura.",
        },
        "aboutBinauralBeats": {"benefits": {"subtitle": "Beats binaurais, tons isocrônicos, portadoras Solfeggio e camadas de ruído podem apoiar foco, relaxamento, sono, meditação, criatividade e humor."}},
    },
    "ru": {
        "meta": {"title": "MindState: Свои биты и шум", "description": "Создавайте многослойные звуковые миксы с бинауральными, моноауральными и изохронными битами, шумом, эффектами и аудиоклипами. 33 встроенных микса, редакторы Quick и Full, QR-обмен и Daily Rituals."},
        "nav": {"pricing": "Цены", "faq": "Частые вопросы"},
        "hero": {"subtitle": "Свои биты и шум для отдыха, фокуса, медитации, творчества и лучшего сна. Если вам нужно облегчение симптомов СДВГ, более глубокая медитация, лучший сон, больше творчества или острее фокус, MindState даёт инструменты для миксов под ваши задачи.", "tagline": "Доступно на Android с профессиональным качеством звука. Бесплатно попробовать."},
        "store": {"playStore": "Скачать в Google Play"},
        "features": {
            "titlePrefix": "Создавайте", "titleHighlight": "многослойные", "titleSuffix": "миксы",
            "pitch": "В отличие от приложений только с пресетами, MindState даёт профессиональный контроль над каждым слоем, частотой и огибающей громкости или начните с 33 встроенных миксов в девяти категориях. Делитесь миксами через QR, планируйте Daily Rituals и слушайте с экраном блокировки и нативным звуком на движке синтеза Rust.",
            "title": "Главные возможности", "subtitle": "Профессиональные инструменты для фокуса, релакса, сна, медитации и творчества.",
            "feature1": {"title": "Редактор Quick и редактор Full", "description": "Quick editor: до четырёх слотов тона, шума, эффекта или файла с живым предпросмотром и выбором битов. Full editor: неограниченные дорожки, огибающие громкости, автоматизация шума и типы дорожек. Переключайтесь между редакторами без потери работы."},
            "feature2": {"title": "Многослойный микс", "description": "Сочетайте бинауральные, моноауральные и изохронные биты; белый, розовый, коричневый, зелёный и цветной шум; эффекты (дождь, океан, ветер, вентилятор, водопад, старая пластинка); таймированные MP3, WAV или FLAC, каждый со своей громкостью."},
            "feature3": {"title": "33 встроенных микса", "description": "Подборка в Сон, Фокус, Медитация, Релакс, Творчество, Настроение, Учёба и Relaxed kid. 17 бесплатно; 16 расширенных по подписке Starter. Дублируйте любой встроенный микс для настройки."},
            "feature4": {"title": "QR-код и ссылка", "description": "Кодируйте миксы как URL mindstate://. Сканируйте, предпросматривайте, редактируйте и сохраняйте. QR с логотипом на белом фоне. Ссылки несут только структуру микса (без своего арта и импортированных файлов)."},
            "feature5": {"title": "Daily Rituals", "description": "Планируйте микс по времени и дням повтора. Создайте ритуал с панели плеера или экрана Rituals. Открывает основной плеер с управлением на экране блокировки в нужное время."},
            "feature6": {"title": "Профессиональный нативный звук", "description": "Синтез Rust в реальном времени с непрерывной фазой, плавными переходами и плавное затухание без щелчков. Воспроизведение, пауза и перемотка на экране блокировки, Smart Pause с наушниками и арт по категориям."},
        },
        "howItWorks": {
            "subtitle": "Просмотр, создание, настройка, сохранение и прослушивание в пять шагов",
            "step1": {"title": "Обзор или создание", "description": "Начните с встроенных миксов или пустого Quick или Full editor."},
            "step2": {"title": "Добавить слои", "description": "Добавьте тоны, шум, эффекты или свои файлы. Выбирайте типы на иллюстрированных чипах в листе добавления дорожки Full editor."},
            "step3": {"title": "Настроить", "description": "Задайте несущую и битовую частоты, несущие Solfeggio и громкости. Огибающие и автоматизация шума в Full editor."},
            "step4": {"title": "Предпросмотр и сохранение", "description": "Живой предпросмотр при редактировании. Сохраняйте свои миксы в Мои миксы с подпиской Starter."},
            "step5": {"title": "Слушать, делиться, планировать", "description": "Воспроизведение с экраном блокировки, обмен по QR или ссылке и опциональный Daily Ritual."},
        },
        "screenshots": {
            "subtitle": "Интерфейс Material 3 со светлой и тёмной темой. Приложение на 7 языках.",
            "player": "Слушайте с управлением на экране блокировки", "mixes": "Встроенные и свои миксы",
            "beatPicker": "Диапазоны волн мозга и тоны Solfeggio", "quickEditor": "Микс в четырёх слотах",
            "shareQr": "Делитесь миксами по QR или ссылке", "addTrack": "Тоны, шум, эффекты и файлы",
            "fullEditor": "Полный контроль каждой дорожки", "ritualsList": "Планируйте Daily Rituals", "ritualEdit": "Время, дни повтора и микс",
        },
        "cta": {
            "subtitle": "Начните с 17 бесплатных встроенных миксов или откройте Starter для безлимитного сохранения и расширенного контента.",
            "benefit1": {"title": "✓ 17 бесплатных миксов", "description": "Воспроизведение встроенных, импорт по QR и дублирование для настройки"},
            "benefit2": {"title": "✓ Подписка Starter", "description": "Безлимитное сохранение своих миксов и 16 расширенных встроенных"},
            "benefit3": {"title": "✓ Профессиональный звук", "description": "Движок синтеза Rust с управлением на экране блокировки"},
        },
        "footer": {"description": "Свои биты и шум для фокуса, релакса, сна, медитации и творчества.", "downloadDescription": "В Google Play. iOS скоро."},
        "pricing": {
            "title": "Цены", "subtitle": "Начните бесплатно; обновитесь, когда нужно сохранять свои миксы и играть расширенный контент.",
            "free": {"name": "Бесплатно", "price": "$0", "description": "Изучайте MindState без предоплаты.", "feature1": "17 встроенных миксов", "feature2": "Просмотр и импорт по QR", "feature3": "Дублирование встроенных с предпросмотром", "feature4": "Онбординг и справочный контент"},
            "starter": {"name": "Starter", "price": "Ежемесячно или ежегодно", "description": "Полный доступ с пробным периодом из магазина.", "feature1": "Безлимитное сохранение своих миксов", "feature2": "16 расширенных встроенных миксов", "feature3": "Daily Rituals из плеера", "feature4": "Планы в Google Play"},
            "samplePacks": {"name": "Пакеты сэмплов", "price": "Разовая покупка", "description": "Опциональные аудиопаки для дополнительных file-track.", "feature1": "Пример: Chakra Bar Chimes (7 тонов)", "feature2": "Добавляет MP3-дорожки в Full editor"},
        },
        "includedMixes": {
            "title": "33 встроенных микса", "subtitle": "Готовые точки старта в девяти категориях. Дублируйте любой микс.",
            "category1": "Сон", "category2": "Фокус", "category3": "Медитация", "category4": "Релакс",
            "category5": "Творчество", "category6": "Настроение", "category7": "Учёба", "category8": "Relaxed kid",
            "note": "17 миксов бесплатно. 16 расширенных требуют подписку Starter.",
        },
        "rituals": {
            "title": "Daily Rituals", "subtitle": "Планируйте микс по времени и дням повтора под ваш распорядок.",
            "bullet1": "Создайте ритуал с экрана Rituals или панели плеера по подписке.",
            "bullet2": "Выберите время, дни повтора и какой микс играть.",
            "bullet3": "Android: надёжные будильники с подсказками режима «Не беспокоить».",
            "bullet4": "iOS: локальные уведомления. Ритуалы перепланируются при смене часового пояса.",
        },
        "faq": {
            "title": "Частые вопросы",
            "q1": "Какие аудиофайлы можно импортировать?", "a1": "MP3, WAV и FLAC с устройства или из встроенных и sample-pack ресурсов.",
            "q2": "Включают ли QR мой пользовательский звук?", "a2": "Нет. QR и ссылки только со структурой микса (тоны, шум, эффекты). После импорта снова прикрепите file-track.",
            "q3": "Как работают Daily Rituals на Android?", "a3": "Будильники и уведомления. Разрешите точный будильник, батарею и уведомления. Опциональный доступ к DND для воспроизведения в режиме «Не беспокоить».",
            "q4": "Как работают Daily Rituals на iOS?", "a4": "Локальные уведомления. Нажмите alert, чтобы открыть MindState и воспроизвести микс.",
            "q5": "Можно ли создать ритуал из текущего микса?", "a5": "Да. Create ritual на панели плеера по подписке.",
        },
        "aboutBinauralBeats": {"benefits": {"subtitle": "Бинауральные биты, изохронные тоны, несущие Solfeggio и шумовые подложки могут поддерживать фокус, релакс, сон, медитацию, творчество и настроение."}},
    },
    "zh": {
        "meta": {"title": "MindState：自定义节拍与噪声", "description": "设计多层声音混音，含双耳、单耳与等时节拍、噪声、环境效果与音频片段。33 个内置混音、Quick 与 Full 编辑器、二维码分享和 Daily Rituals。"},
        "nav": {"pricing": "定价", "faq": "常见问题"},
        "hero": {"subtitle": "自定义节拍与噪声，用于放松、专注、冥想、创意与更好睡眠。无论您是想缓解 AD/HD 症状、更深冥想、更好睡眠、提升创意还是更敏锐专注，MindState 都提供工具，帮您设计量身定制的混音。", "tagline": "Android 可用，专业音质。免费试用。"},
        "store": {"playStore": "在 Google Play 获取"},
        "features": {
            "titlePrefix": "创建个性化", "titleHighlight": "多层", "titleSuffix": "混音",
            "pitch": "不同于只有预设的健康应用，MindState 让您专业控制每一层、频率和音量包络，或从九个类别的 33 个内置混音开始。通过二维码分享混音、安排 Daily Rituals，并用锁屏控制和 Rust 合成引擎的原生音质收听。",
            "title": "主要功能", "subtitle": "用于专注、放松、睡眠、冥想与创意的专业工具。",
            "feature1": {"title": "Quick editor 与 Full editor", "description": "Quick editor：最多四个音调、噪声、效果或文件槽位，带实时预览与节拍选择器。Full editor：无限轨道、音量包络、噪声自动化和分类添加轨道类型。切换编辑器不丢失工作。"},
            "feature2": {"title": "多层混音", "description": "组合双耳、单耳与等时节拍；白、粉、棕、绿与彩色噪声；环境效果（雨、海洋、风、风扇、瀑布、老唱片）；以及定时 MP3、WAV 或 FLAC 片段，各自独立音量。"},
            "feature3": {"title": "33 个内置混音", "description": "涵盖睡眠、专注、冥想、放松、创意、情绪、学习与 Relaxed kid 的精选混音。17 个免费播放；16 个扩展混音需 Starter 订阅。复制任意内置混音即可自定义。"},
            "feature4": {"title": "二维码与链接分享", "description": "将混音编码为 mindstate:// URL。扫描、预览、编辑并保存。白底品牌二维码。分享链接仅含混音结构（不含自定义封面与导入音频文件）。"},
            "feature5": {"title": "Daily Rituals", "description": "按时间与重复日安排混音。从播放器工具栏或 Rituals 屏幕创建仪式。到点收听时打开主播放器并支持锁屏控制。"},
            "feature6": {"title": "专业原生音频", "description": "Rust 实时合成，相位连续、平滑滑音与防咔嗒淡入淡出。锁屏播放、暂停与快进，耳机 Smart Pause，以及按类别的混音封面。"},
        },
        "howItWorks": {
            "subtitle": "五步完成浏览、创建、调节、保存与收听",
            "step1": {"title": "浏览或创建", "description": "从内置混音或空白 Quick 或 Full 编辑器开始。"},
            "step2": {"title": "添加层", "description": "添加音调、噪声、环境效果或您的音频文件。在 Full 编辑器添加轨道页通过插图芯片选择类型。"},
            "step3": {"title": "调节", "description": "设置载波与节拍频率、Solfeggio 载波与音量。在 Full 编辑器中塑造包络与噪声自动化。"},
            "step4": {"title": "预览并保存", "description": "编辑时实时预览。通过 Starter 订阅将自定义混音保存到「我的混音」。"},
            "step5": {"title": "收听、分享、安排", "description": "锁屏控制播放，通过二维码或链接分享，并可选择安排 Daily Ritual。"},
        },
        "screenshots": {
            "subtitle": "Material 3 界面，浅色与深色模式。应用支持 7 种语言。",
            "player": "锁屏控制收听", "mixes": "浏览内置与自定义混音",
            "beatPicker": "选择脑波频段与 Solfeggio 音调", "quickEditor": "四个槽位构建混音",
            "shareQr": "通过二维码或链接分享混音", "addTrack": "添加音调、噪声、效果与文件",
            "fullEditor": "完全控制每条轨道", "ritualsList": "安排 Daily Rituals", "ritualEdit": "时间、重复日与混音",
        },
        "cta": {
            "subtitle": "从 17 个免费内置混音开始，或解锁 Starter 以保存无限自定义混音并播放扩展内容。",
            "benefit1": {"title": "✓ 17 个免费混音", "description": "播放内置混音、二维码导入并复制自定义"},
            "benefit2": {"title": "✓ Starter 订阅", "description": "保存无限自定义混音并播放 16 个扩展内置混音"},
            "benefit3": {"title": "✓ 专业音频", "description": "Rust 合成引擎与锁屏播放控制"},
        },
        "footer": {"description": "用于专注、放松、睡眠、冥想与创意的自定义节拍与噪声。", "downloadDescription": "Google Play 可用。iOS 即将推出。"},
        "pricing": {
            "title": "定价", "subtitle": "免费开始；需要保存自定义混音并播放扩展内置内容时再升级。",
            "free": {"name": "免费", "price": "¥0", "description": "无需预付费用即可体验 MindState。", "feature1": "播放 17 个内置混音", "feature2": "浏览并通过二维码导入混音", "feature3": "复制内置混音并预览编辑", "feature4": "引导与关于内容"},
            "starter": {"name": "Starter", "price": "月付或年付", "description": "商店管理的免费试用解锁完整访问。", "feature1": "保存无限自定义混音", "feature2": "播放 16 个扩展内置混音", "feature3": "从播放器创建 Daily Rituals", "feature4": "通过 Google Play 的月付与年付计划"},
            "samplePacks": {"name": "采样包", "price": "一次性购买", "description": "可选音频包，用于额外文件轨道声音。", "feature1": "示例：Chakra Bar Chimes（7 个音调）", "feature2": "向 Full 编辑器添加 MP3 文件轨道"},
        },
        "includedMixes": {
            "title": "33 个内置混音", "subtitle": "九个类别的精选起点。复制任意混音即可拥有。",
            "category1": "睡眠", "category2": "专注", "category3": "冥想", "category4": "放松",
            "category5": "创意", "category6": "情绪", "category7": "学习", "category8": "Relaxed kid",
            "note": "17 个混音免费播放。16 个扩展混音需 Starter 订阅。",
        },
        "rituals": {
            "title": "Daily Rituals", "subtitle": "按时间与重复日安排混音，让收听融入日常。",
            "bullet1": "订阅后从 Rituals 屏幕或播放器工具栏创建仪式。",
            "bullet2": "选择时间、重复日与要播放的混音。",
            "bullet3": "Android 使用可靠闹钟调度，可选勿扰模式指引。",
            "bullet4": "iOS 使用本地通知。跨时区旅行时会重新安排仪式。",
        },
        "faq": {
            "title": "常见问题",
            "q1": "可以导入哪些音频文件？", "a1": "来自设备存储或捆绑与采样包资源的 MP3、WAV 和 FLAC。",
            "q2": "二维码是否包含我的自定义音频？", "a2": "不包含。二维码与分享链接仅含混音结构（音调、噪声、效果）。导入后请重新附加文件轨道。",
            "q3": "Android 上 Daily Rituals 如何工作？", "a3": "闹钟与通知。请在提示时授予精确闹钟、电池与通知权限。可选勿扰访问可在 DND 期间继续播放。",
            "q4": "iOS 上 Daily Rituals 如何工作？", "a4": "本地通知。点按提醒打开 MindState 并播放预定混音。",
            "q5": "能否从正在播放的混音创建仪式？", "a5": "可以。订阅后使用播放器工具栏上的 Create ritual。",
        },
        "aboutBinauralBeats": {"benefits": {"subtitle": "双耳节拍、等时音调、Solfeggio 载波与噪声底层可支持专注、放松、睡眠、冥想、创意与情绪。"}},
    },
    "hi": {
        "meta": {"title": "MindState: कस्टम बीट्स और नॉइज़", "description": "बाइनोरल, मोनोरल और आइसोक्रोनिक बीट्स, नॉइज़, एंबिएंट इफ़ेक्ट और ऑडियो क्लिप के साथ मल्टी-लेयर साउंड मिक्स बनाएं। 33 शामिल मिक्स, Quick और Full एडिटर, QR शेयरिंग और Daily Rituals।"},
        "nav": {"pricing": "मूल्य", "faq": "अक्सर पूछे जाने वाले प्रश्न"},
        "hero": {"subtitle": "आराम, फ़ोकस, ध्यान, रचनात्मकता और बेहतर नींद के लिए कस्टम बीट्स और नॉइज़। चाहे AD/HD लक्षणों से राहत, गहरा ध्यान, बेहतर नींद, अधिक रचनात्मकता या तेज़ फ़ोकस चाहिए, MindState आपकी ज़रूरतों के अनुसार मिक्स डिज़ाइन करने के टूल देता है।", "tagline": "Android पर प्रोफ़ेशनल ऑडियो क्वालिटी के साथ उपलब्ध। मुफ़्त में आज़माएं।"},
        "store": {"playStore": "Google Play पर पाएं"},
        "features": {
            "titlePrefix": "व्यक्तिगत", "titleHighlight": "मल्टी-लेयर", "titleSuffix": "मिक्स बनाएं",
            "pitch": "सिर्फ़ प्रीसेट वाले ऐप्स के विपरीत, MindState हर लेयर, फ़्रीक्वेंसी और वॉल्यूम एनवेलोप पर प्रोफ़ेशनल नियंत्रण देता है, या नौ श्रेणियों में 33 शामिल मिक्स से शुरू करें। QR से मिक्स शेयर करें, Daily Rituals शेड्यूल करें, और लॉक स्क्रीन कंट्रोल व Rust सिंथेसिस इंजन के साथ नेटिव ऑडियो सुनें।",
            "title": "मुख्य फ़ीचर", "subtitle": "फ़ोकस, आराम, नींद, ध्यान और रचनात्मकता के लिए प्रोफ़ेशनल टूल।",
            "feature1": {"title": "Quick editor और Full editor", "description": "Quick editor: लाइव प्रीव्यू और बीट पिकर के साथ चार टोन, नॉइज़, इफ़ेक्ट या फ़ाइल स्लॉट। Full editor: असीमित ट्रैक, वॉल्यूम एनवेलोप, नॉइज़ ऑटोमेशन और श्रेणीबद्ध ऐड-ट्रैक प्रकार। बिना काम खोए एडिटर बदलें।"},
            "feature2": {"title": "मल्टी-लेयर मिक्सिंग", "description": "बाइनोरल, मोनोरल और आइसोक्रोनिक बीट्स; सफ़ेद, गुलाबी, भूरा, हरा और रंगीन नॉइज़; एंबिएंट इफ़ेक्ट (बारिश, समुद्र, हवा, पंखा, झरना, पुराना रिकॉर्ड); और टाइम्ड MP3, WAV या FLAC क्लिप, हर एक का अलग वॉल्यूम।"},
            "feature3": {"title": "33 शामिल मिक्स", "description": "नींद, फ़ोकस, ध्यान, आराम, रचनात्मकता, मूड, अध्ययन और Relaxed kid में क्यूरेटेड मिक्स। 17 मुफ़्त; Starter सब्सक्रिप्शन पर 16 विस्तारित। किसी भी शामिल मिक्स को डुप्लिकेट करके कस्टमाइज़ करें।"},
            "feature4": {"title": "QR कोड और लिंक शेयरिंग", "description": "मिक्स को mindstate:// URL के रूप में एन्कोड करें। स्कैन, प्रीव्यू, एडिट और सेव करें। सफ़ेद पृष्ठभूमि पर लोगो वाला QR। लिंक में सिर्फ़ मिक्स संरचना (कस्टम आर्ट और इम्पोर्टेड ऑडियो फ़ाइलें शामिल नहीं)।"},
            "feature5": {"title": "Daily Rituals", "description": "समय और दोहराव वाले दिनों पर मिक्स शेड्यूल करें। प्लेयर टूलबार या Rituals स्क्रीन से रिचुअल बनाएं। सुनने के समय लॉक स्क्रीन ट्रांसपोर्ट के साथ मुख्य प्लेयर खुलता है।"},
            "feature6": {"title": "प्रोफ़ेशनल नेटिव ऑडियो", "description": "Rust रियल-टाइम सिंथेसिस, फेज-निरंतर टोन, स्मूथ ग्लाइड और एंटी-क्लिक फ़ेड। लॉक स्क्रीन प्ले, पॉज़ और सीक, हेडसेट Smart Pause, और श्रेणी थीम आर्टवर्क।"},
        },
        "howItWorks": {
            "subtitle": "पाँच चरणों में ब्राउज़, बनाएं, ट्यून, सेव और सुनें",
            "step1": {"title": "ब्राउज़ या बनाएं", "description": "शामिल मिक्स या खाली Quick या Full एडिटर से शुरू करें।"},
            "step2": {"title": "लेयर जोड़ें", "description": "टोन, नॉइज़, एंबिएंट इफ़ेक्ट या अपनी ऑडियो फ़ाइलें जोड़ें। Full एडिटर ऐड-ट्रैक शीट में चित्रित चिप्स से प्रकार चुनें।"},
            "step3": {"title": "ट्यून करें", "description": "कैरियर और बीट फ़्रीक्वेंसी, Solfeggio कैरियर और वॉल्यूम सेट करें। Full एडिटर में एनवेलोप और नॉइज़ ऑटोमेशन।"},
            "step4": {"title": "प्रीव्यू और सेव", "description": "एडिट करते समय लाइव प्रीव्यू। Starter सब्सक्रिप्शन पर मेरे मिक्स में कस्टम मिक्स सेव करें।"},
            "step5": {"title": "सुनें, शेयर, शेड्यूल", "description": "लॉक स्क्रीन कंट्रोल से चलाएं, QR या लिंक से शेयर करें, और वैकल्पिक Daily Ritual शेड्यूल करें।"},
        },
        "screenshots": {
            "subtitle": "लाइट और डार्क मोड के साथ Material 3 इंटरफ़ेस। ऐप 7 भाषाओं में।",
            "player": "लॉक स्क्रीन कंट्रोल से सुनें", "mixes": "शामिल और कस्टम मिक्स ब्राउज़ करें",
            "beatPicker": "ब्रेनवेव बैंड और Solfeggio टोन चुनें", "quickEditor": "चार स्लॉट में मिक्स बनाएं",
            "shareQr": "QR या लिंक से मिक्स शेयर करें", "addTrack": "टोन, नॉइज़, इफ़ेक्ट और फ़ाइलें जोड़ें",
            "fullEditor": "हर ट्रैक पर पूरा नियंत्रण", "ritualsList": "Daily Rituals शेड्यूल करें", "ritualEdit": "समय, दोहराव दिन और मिक्स",
        },
        "cta": {
            "subtitle": "17 मुफ़्त शामिल मिक्स से शुरू करें, या असीमित कस्टम मिक्स सेव और विस्तारित कंटेंट के लिए Starter अनलॉक करें।",
            "benefit1": {"title": "✓ 17 मुफ़्त मिक्स", "description": "शामिल मिक्स चलाएं, QR से इम्पोर्ट करें, कस्टमाइज़ के लिए डुप्लिकेट करें"},
            "benefit2": {"title": "✓ Starter सब्सक्रिप्शन", "description": "असीमित कस्टम मिक्स सेव करें और 16 विस्तारित शामिल मिक्स चलाएं"},
            "benefit3": {"title": "✓ प्रोफ़ेशनल ऑडियो", "description": "लॉक स्क्रीन कंट्रोल के साथ Rust सिंथेसिस इंजन"},
        },
        "footer": {"description": "फ़ोकस, आराम, नींद, ध्यान और रचनात्मकता के लिए कस्टम बीट्स और नॉइज़।", "downloadDescription": "Google Play पर उपलब्ध। iOS जल्द।"},
        "pricing": {
            "title": "मूल्य", "subtitle": "मुफ़्त शुरू करें; कस्टम मिक्स सेव और विस्तारित शामिल कंटेंट चलाने के लिए अपग्रेड करें।",
            "free": {"name": "मुफ़्त", "price": "₹0", "description": "बिना अग्रिम लागत MindState एक्सप्लोर करें।", "feature1": "17 शामिल मिक्स चलाएं", "feature2": "QR से मिक्स ब्राउज़ और इम्पोर्ट", "feature3": "शामिल मिक्स डुप्लिकेट और प्रीव्यू के साथ एडिट", "feature4": "ऑनबोर्डिंग और about कंटेंट"},
            "starter": {"name": "Starter", "price": "मासिक या वार्षिक", "description": "स्टोर-प्रबंधित मुफ़्त ट्रायल के साथ पूर्ण एक्सेस।", "feature1": "असीमित कस्टम मिक्स सेव", "feature2": "16 विस्तारित शामिल मिक्स चलाएं", "feature3": "प्लेयर से Daily Rituals बनाएं", "feature4": "Google Play पर मासिक और वार्षिक प्लान"},
            "samplePacks": {"name": "सैंपल पैक", "price": "एक बार की खरीद", "description": "अतिरिक्त फ़ाइल-ट्रैक ध्वनियों के लिए वैकल्पिक ऑडियो पैक।", "feature1": "उदाहरण: Chakra Bar Chimes (7 टोन)", "feature2": "Full एडिटर में MP3 फ़ाइल ट्रैक जोड़ता है"},
        },
        "includedMixes": {
            "title": "33 शामिल मिक्स", "subtitle": "नौ श्रेणियों में क्यूरेटेड शुरुआती बिंदु। कोई भी मिक्स डुप्लिकेट कर अपना बनाएं।",
            "category1": "नींद", "category2": "फ़ोकस", "category3": "ध्यान", "category4": "आराम",
            "category5": "रचनात्मकता", "category6": "मूड", "category7": "अध्ययन", "category8": "Relaxed kid",
            "note": "17 मिक्स मुफ़्त चलाने के लिए। 16 विस्तारित के लिए Starter सब्सक्रिप्शन।",
        },
        "rituals": {
            "title": "Daily Rituals", "subtitle": "समय और दोहराव वाले दिनों पर मिक्स शेड्यूल करें ताकि सुनना आपकी दिनचर्या में फिट हो।",
            "bullet1": "सब्सक्रिप्शन पर Rituals स्क्रीन या प्लेयर टूलबार से रिचुअल बनाएं।",
            "bullet2": "समय, दोहराव दिन और कौन सा मिक्स चले, चुनें।",
            "bullet3": "Android विश्वसनीय अलार्म शेड्यूलिंग और वैकल्पिक DND मार्गदर्शन।",
            "bullet4": "iOS स्थानीय सूचनाएं। समय क्षेत्र बदलने पर रिचुअल पुनः शेड्यूल।",
        },
        "faq": {
            "title": "अक्सर पूछे जाने वाले प्रश्न",
            "q1": "कौन सी ऑडियो फ़ाइलें इम्पोर्ट कर सकता हूँ?", "a1": "डिवाइस स्टोरेज या बंडल और सैंपल-पैक संपत्तियों से MP3, WAV और FLAC।",
            "q2": "क्या QR में मेरा कस्टम ऑडियो शामिल है?", "a2": "नहीं। QR और शेयर लिंक में सिर्फ़ मिक्स संरचना (टोन, नॉइज़, इफ़ेक्ट)। इम्पोर्ट के बाद फ़ाइल ट्रैक फिर जोड़ें।",
            "q3": "Android पर Daily Rituals कैसे काम करते हैं?", "a3": "अलार्म और सूचनाएं। सटीक अलार्म, बैटरी और सूचना अनुमति दें। वैकल्पिक DND एक्सेस DND के दौरान प्लेबैक जारी रख सकता है।",
            "q4": "iOS पर Daily Rituals कैसे काम करते हैं?", "a4": "स्थानीय सूचनाएं। शेड्यूल मिक्स चलाने के लिए अलर्ट टैप कर MindState खोलें।",
            "q5": "क्या चल रहे मिक्स से रिचुअल बना सकता हूँ?", "a5": "हाँ। सब्सक्रिप्शन पर प्लेयर टूलबार पर Create ritual उपयोग करें।",
        },
        "aboutBinauralBeats": {"benefits": {"subtitle": "बाइनोरल बीट्स, आइसोक्रोनिक टोन, Solfeggio कैरियर और नॉइज़ बेड फ़ोकस, आराम, नींद, ध्यान, रचनात्मकता और मूड में सहायक हो सकते हैं।"}},
    },
    "id": {
        "meta": {"title": "MindState: Beat & noise kustom", "description": "Rancang mix suara berlapis dengan beat binaural, monaural, dan isokronik, noise, efek ambient, dan klip audio. 33 mix termasuk, editor Quick dan Full, berbagi QR, dan Daily Rituals."},
        "nav": {"pricing": "Harga", "faq": "FAQ"},
        "hero": {"subtitle": "Beat dan noise kustom untuk rileks, fokus, meditasi, kreativitas, dan tidur lebih nyenyak. Baik Anda mencari ringan gejala AD/HD, meditasi lebih dalam, tidur lebih baik, kreativitas lebih tinggi, atau fokus lebih tajam, MindState memberi alat untuk merancang mix sesuai kebutuhan Anda.", "tagline": "Tersedia di Android dengan kualitas audio profesional. Gratis untuk dicoba."},
        "store": {"playStore": "Dapatkan di Google Play"},
        "features": {
            "titlePrefix": "Buat mix", "titleHighlight": "berlapis", "titleSuffix": "personal",
            "pitch": "Berbeda dari app wellness berbasis preset saja, MindState memberi kontrol profesional atas setiap lapisan, frekuensi, dan envelope volume, atau mulai dari 33 mix termasuk dalam sembilan kategori. Bagikan mix via QR, jadwalkan Daily Rituals, dan dengarkan dengan kontrol layar kunci dan audio native dengan mesin sintesis Rust.",
            "title": "Fitur utama", "subtitle": "Alat profesional untuk fokus, relaksasi, tidur, meditasi, dan kreativitas.",
            "feature1": {"title": "Editor Quick dan editor Full", "description": "Editor Quick: hingga empat slot nada, noise, efek, atau file dengan pratinjau langsung dan pemilih beat. Editor Full: trek tak terbatas, envelope volume, otomasi noise, dan jenis tambah trek terkategori. Ganti editor tanpa kehilangan pekerjaan."},
            "feature2": {"title": "Mixing berlapis", "description": "Gabungkan beat binaural, monaural, dan isokronik; noise putih, merah muda, cokelat, hijau, dan berwarna; efek ambient (hujan, laut, angin, kipas, air terjun, rekaman lama); dan klip MP3, WAV, atau FLAC berwaktu, masing-masing volume independen."},
            "feature3": {"title": "33 mix termasuk", "description": "Mix kurasi di Tidur, Fokus, Meditasi, Relaksasi, Kreativitas, Suasana hati, Belajar, dan Relaxed kid. 17 gratis; 16 extended dengan langganan Starter. Duplikasi mix termasuk mana pun untuk menyesuaikan."},
            "feature4": {"title": "Kode QR dan berbagi tautan", "description": "Enkode mix sebagai URL mindstate://. Pindai, pratinjau, edit, dan simpan. QR bermerek di latar putih. Tautan hanya membawa struktur mix (bukan seni kustom atau file audio impor)."},
            "feature5": {"title": "Daily Rituals", "description": "Jadwalkan mix menurut waktu dan hari ulang. Buat ritual dari toolbar pemutar atau layar Rituals. Membuka pemutar utama dengan transport layar kunci saat waktunya mendengarkan."},
            "feature6": {"title": "Audio native profesional", "description": "Sintesis Rust real-time dengan nada fase kontinyu, glide halus, dan fade anti-klik. Putar, jeda, dan seek di layar kunci, Smart Pause headset, dan artwork mix per kategori."},
        },
        "howItWorks": {
            "subtitle": "Jelajahi, buat, sesuaikan, simpan, dan dengarkan dalam lima langkah",
            "step1": {"title": "Jelajahi atau buat", "description": "Mulai dari mix termasuk atau editor Quick atau Full kosong."},
            "step2": {"title": "Tambah lapisan", "description": "Tambah nada, noise, efek ambient, atau file audio Anda. Pilih jenis dari chip bergambar di lembar tambah trek editor Full."},
            "step3": {"title": "Sesuaikan", "description": "Atur frekuensi pembawa dan beat, pembawa Solfeggio, dan volume. Bentuk envelope dan otomasi noise di editor Full."},
            "step4": {"title": "Pratinjau dan simpan", "description": "Pratinjau langsung saat mengedit. Simpan mix kustom ke Mix saya dengan langganan Starter."},
            "step5": {"title": "Dengarkan, bagikan, jadwalkan", "description": "Putar dengan kontrol layar kunci, bagikan via QR atau tautan, dan opsional jadwalkan Daily Ritual."},
        },
        "screenshots": {
            "subtitle": "Antarmuka Material 3 mode terang dan gelap. App dalam 7 bahasa.",
            "player": "Dengarkan dengan kontrol layar kunci", "mixes": "Jelajahi mix termasuk dan kustom",
            "beatPicker": "Pilih pita gelombang otak dan nada Solfeggio", "quickEditor": "Buat mix dalam empat slot",
            "shareQr": "Bagikan mix via QR atau tautan", "addTrack": "Tambah nada, noise, efek, dan file",
            "fullEditor": "Kontrol penuh setiap trek", "ritualsList": "Jadwalkan Daily Rituals", "ritualEdit": "Waktu, hari ulang, dan mix",
        },
        "cta": {
            "subtitle": "Mulai dengan 17 mix termasuk gratis, atau buka Starter untuk menyimpan mix kustom tak terbatas dan memutar konten extended.",
            "benefit1": {"title": "✓ 17 mix gratis", "description": "Putar mix termasuk, impor via QR, dan duplikasi untuk menyesuaikan"},
            "benefit2": {"title": "✓ Langganan Starter", "description": "Simpan mix kustom tak terbatas dan putar 16 mix termasuk extended"},
            "benefit3": {"title": "✓ Audio profesional", "description": "Mesin sintesis Rust dengan kontrol layar kunci"},
        },
        "footer": {"description": "Beat dan noise kustom untuk fokus, relaksasi, tidur, meditasi, dan kreativitas.", "downloadDescription": "Tersedia di Google Play. iOS segera."},
        "pricing": {
            "title": "Harga", "subtitle": "Mulai gratis; upgrade saat ingin menyimpan mix kustom dan memutar konten termasuk extended.",
            "free": {"name": "Gratis", "price": "Rp 0", "description": "Jelajahi MindState tanpa biaya di muka.", "feature1": "Putar 17 mix termasuk", "feature2": "Jelajahi dan impor mix via QR", "feature3": "Duplikasi mix termasuk dan edit dengan pratinjau", "feature4": "Onboarding dan konten tentang app"},
            "starter": {"name": "Starter", "price": "Bulanan atau tahunan", "description": "Akses penuh dengan uji coba gratis dari toko.", "feature1": "Simpan mix kustom tak terbatas", "feature2": "Putar 16 mix termasuk extended", "feature3": "Buat Daily Rituals dari pemutar", "feature4": "Paket bulanan dan tahunan via Google Play"},
            "samplePacks": {"name": "Paket sampel", "price": "Pembelian sekali", "description": "Paket audio opsional untuk suara trek file tambahan.", "feature1": "Contoh: Chakra Bar Chimes (7 nada)", "feature2": "Menambah trek MP3 ke editor Full"},
        },
        "includedMixes": {
            "title": "33 mix termasuk", "subtitle": "Titik awal kurasi di sembilan kategori. Duplikasi mix mana pun agar menjadi milik Anda.",
            "category1": "Tidur", "category2": "Fokus", "category3": "Meditasi", "category4": "Relaksasi",
            "category5": "Kreativitas", "category6": "Suasana hati", "category7": "Belajar", "category8": "Relaxed kid",
            "note": "17 mix gratis diputar. 16 extended memerlukan langganan Starter.",
        },
        "rituals": {
            "title": "Daily Rituals", "subtitle": "Jadwalkan mix menurut waktu dan hari ulang agar cocok dengan rutinitas Anda.",
            "bullet1": "Buat ritual dari layar Rituals atau toolbar pemutar saat berlangganan.",
            "bullet2": "Pilih waktu, hari ulang, dan mix yang diputar.",
            "bullet3": "Android memakai penjadwalan alarm andal dengan panduan opsional Jangan Ganggu.",
            "bullet4": "iOS memakai notifikasi lokal. Ritual dijadwalkan ulang saat Anda pindah zona waktu.",
        },
        "faq": {
            "title": "Pertanyaan yang sering diajukan",
            "q1": "File audio apa yang bisa saya impor?", "a1": "MP3, WAV, dan FLAC dari penyimpanan perangkat atau aset bundel dan paket sampel.",
            "q2": "Apakah kode QR menyertakan audio kustom saya?", "a2": "Tidak. QR dan tautan hanya menyertakan struktur mix (nada, noise, efek). Lampirkan kembali trek file setelah impor.",
            "q3": "Bagaimana Daily Rituals bekerja di Android?", "a3": "Alarm dan notifikasi. Berikan izin alarm tepat, baterai, dan notifikasi saat diminta. Akses opsional ke DND memungkinkan pemutaran saat DND.",
            "q4": "Bagaimana Daily Rituals bekerja di iOS?", "a4": "Notifikasi lokal. Ketuk alert untuk membuka MindState dan memutar mix terjadwal.",
            "q5": "Bisakah saya membuat ritual dari mix yang sedang diputar?", "a5": "Ya. Gunakan Create ritual di toolbar pemutar saat berlangganan.",
        },
        "aboutBinauralBeats": {"benefits": {"subtitle": "Beat binaural, nada isokronik, pembawa Solfeggio, dan lapisan noise dapat mendukung fokus, relaksasi, tidur, meditasi, kreativitas, dan suasana hati."}},
    },
}


def main() -> None:
    for locale, overlay in OVERLAYS.items():
        path = ROOT / f"{locale}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        merged = deep_merge(data, overlay)
        path.write_text(
            json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Updated {path}")


if __name__ == "__main__":
    main()
