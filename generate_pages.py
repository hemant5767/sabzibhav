#!/usr/bin/env python3
"""
Generates 10 SEO-targeted mandi-bhav HTML pages from one shared template.
Each page targets one keyword, has unique title/meta/H1/copy, and pulls
LIVE price data client-side via mandi-data.js (no stored data).
"""
import os

OUT_DIR = "/home/claude/mandi-pages"
SITE_NAME = "MandiBhavToday"
BASE_URL = "https://sabzibhav.in/"  # placeholder — update to the real domain before publishing

NAV_LINKS = [
    ("index.html", "होम"),
    ("mandi-bhav-today.html", "आज का भाव"),
    ("neemuch-mandi-bhav.html", "नीमच"),
    ("indore-mandi-bhav.html", "इंदौर"),
    ("merta-mandi-bhav.html", "मेड़ता"),
    ("harda-mandi-bhav.html", "हरदा"),
    ("kota-mandi-bhav-today.html", "कोटा"),
]

PAGES = [
    {
        "slug": "neemuch-mandi-bhav",
        "keyword": "neemuch mandi bhav",
        "h1": "नीमच मंडी भाव — Neemuch Mandi Bhav Today",
        "title": "नीमच मंडी भाव आज | Neemuch Mandi Bhav Today",
        "meta_description": "नीमच मंडी का आज का ताज़ा भाव — सोयाबीन, चना, लहसुन, धनिया और अन्य फसलों के न्यूनतम, अधिकतम व मोडल रेट। Live Neemuch mandi bhav, daily updated.",
        "state": "Madhya Pradesh",
        "district": "Neemuch",
        "market": "Neemuch",
        "intro": (
            "नीमच मध्य प्रदेश की उन प्रमुख मंडियों में से एक है जहाँ सोयाबीन, चना, लहसुन और धनिया "
            "की बड़ी मात्रा में आवक होती है। यह पेज नीमच मंडी का आज का भाव सीधे एगमार्कनेट "
            "(Agmarknet / data.gov.in) से लाइव दिखाता है — हर बार पेज खोलने पर ताज़ा डेटा।"
        ),
        "body_paras": [
            "नीमच मंडी में लहसुन और धनिया के भाव पूरे मध्य प्रदेश के व्यापारियों और किसानों के लिए एक "
            "बेंचमार्क की तरह काम करते हैं। मंडी भाव रोज़ बदलता है — आवक, मांग और मौसम के हिसाब से, "
            "इसलिए ताज़ा रेट जानना बिक्री का फ़ैसला लेने से पहले ज़रूरी होता है।",
            "नीचे दी गई टेबल में फसल का नाम, किस्म (वैरायटी), मंडी का नाम, और न्यूनतम-अधिकतम-मोडल भाव "
            "रुपये प्रति क्विंटल में दिखाया गया है। मोडल प्राइस वह भाव है जिस पर सबसे ज़्यादा सौदे हुए।",
        ],
    },
    {
        "slug": "indore-mandi-bhav",
        "keyword": "indore mandi bhav",
        "h1": "इंदौर मंडी भाव — Indore Mandi Bhav Today",
        "title": "इंदौर मंडी भाव आज | Indore Mandi Bhav Today",
        "meta_description": "इंदौर मंडी का आज का भाव — सोयाबीन, गेहूं, चना, मक्का व सब्ज़ियों के लाइव रेट। Indore mandi bhav today, updated daily from Agmarknet.",
        "state": "Madhya Pradesh",
        "district": "Indore",
        "market": "Indore",
        "intro": (
            "इंदौर मध्य प्रदेश की सबसे बड़ी और व्यस्त मंडियों में से एक है। यहाँ सोयाबीन, गेहूं, मक्का "
            "और कई सब्ज़ियों का बड़ा कारोबार होता है। यह पेज इंदौर मंडी का आज का भाव सीधे सरकारी "
            "एगमार्कनेट डेटा से लाइव दिखाता है।"
        ),
        "body_paras": [
            "इंदौर मंडी का आकार बड़ा होने की वजह से यहाँ का भाव अक्सर आसपास की छोटी मंडियों के रेट को "
            "भी प्रभावित करता है। व्यापारी और किसान दोनों इंदौर का रेट एक रेफरेंस प्राइस की तरह देखते हैं।",
            "टेबल में हर फसल की किस्म अलग से दिखाई गई है क्योंकि एक ही फसल की अलग-अलग किस्म का भाव "
            "अलग हो सकता है — जैसे सोयाबीन की पीली किस्म और सामान्य किस्म के रेट में अंतर होता है।",
        ],
    },
    {
        "slug": "mandi-bhav-today",
        "keyword": "mandi bhav today",
        "h1": "आज का मंडी भाव — Mandi Bhav Today (All India)",
        "title": "आज का मंडी भाव | Mandi Bhav Today — Live Rates",
        "meta_description": "आज का मंडी भाव लाइव देखें — अपनी मंडी चुनें और न्यूनतम, अधिकतम, मोडल रेट जानें। Mandi bhav today, daily updated from Agmarknet (data.gov.in).",
        "state": "",
        "district": "",
        "market": "",
        "search_default": True,
        "intro": (
            "हर दिन हज़ारों किसान और व्यापारी एक ही सवाल पूछते हैं — \"आज मंडी भाव क्या है?\" यह पेज "
            "आपको किसी भी मंडी का आज का भाव खोजने की सुविधा देता है। नीचे मंडी का नाम टाइप करें और "
            "लाइव रेट देखें।"
        ),
        "body_paras": [
            "मंडी भाव हर मंडी में अलग होता है क्योंकि स्थानीय आवक, माल की क्वालिटी और मांग अलग-अलग होती "
            "है। इसलिए सिर्फ एक औसत भाव देखने के बजाय अपनी नज़दीकी मंडी का सही रेट देखना ज़्यादा फ़ायदेमंद रहता है।",
            "यह डेटा भारत सरकार के एगमार्कनेट पोर्टल से सीधे लिया जाता है, जो देश की मंडियों से रोज़ का "
            "भाव इकट्ठा करता है। कोई भी डेटा यहाँ सेव नहीं किया जाता — हर बार पेज खोलने पर ताज़ा रेट लाया जाता है।",
        ],
    },
    {
        "slug": "mandi-bhav",
        "keyword": "mandi bhav",
        "h1": "मंडी भाव — Mandi Bhav Live Rates",
        "title": "मंडी भाव | Mandi Bhav — Live Crop Prices India",
        "meta_description": "मंडी भाव लाइव देखें — भारत की मंडियों का न्यूनतम, अधिकतम और मोडल रेट। Mandi bhav for wheat, soybean, gram, garlic and more, updated daily.",
        "state": "",
        "district": "",
        "market": "",
        "search_default": True,
        "intro": (
            "\"मंडी भाव\" का मतलब है किसी कृषि उपज मंडी (APMC) में किसी फसल का थोक भाव — यानी जिस "
            "दाम पर व्यापारी किसान से माल खरीदते हैं। यह भाव हर दिन, और कई बार दिन में भी, बदल सकता है।"
        ),
        "body_paras": [
            "मंडी भाव तीन तरह से बताया जाता है — न्यूनतम भाव (Min Price), अधिकतम भाव (Max Price) और "
            "मोडल भाव (Modal Price)। मोडल भाव वह रेट है जिस पर उस दिन सबसे ज़्यादा सौदे हुए, इसलिए इसे "
            "सबसे भरोसेमंद माना जाता है।",
            "इस पेज पर आप किसी भी मंडी, फसल या राज्य का भाव खोज सकते हैं। डेटा सीधे data.gov.in के "
            "एगमार्कनेट API से आता है और कहीं स्टोर नहीं किया जाता।",
        ],
    },
    {
        "slug": "neemuch-mandi-bhav-today",
        "keyword": "neemuch mandi bhav today",
        "h1": "नीमच मंडी भाव आज — Neemuch Mandi Bhav Today (Live)",
        "title": "नीमच मंडी भाव आज लाइव | Neemuch Mandi Bhav Today",
        "meta_description": "नीमच मंडी भाव आज — लहसुन, सोयाबीन, चना, धनिया का लाइव रेट। आज का नीमच मंडी भाव, हर दिन अपडेट।",
        "state": "Madhya Pradesh",
        "district": "Neemuch",
        "market": "Neemuch",
        "intro": (
            "आज नीमच मंडी में क्या भाव चल रहा है? इस पेज पर आज की तारीख़ का ताज़ा भाव — लहसुन, सोयाबीन, "
            "चना और धनिया समेत — सीधे एगमार्कनेट से लाइव दिखाया गया है।"
        ),
        "body_paras": [
            "नीमच जिले की मंडी राजस्थान और मध्य प्रदेश के सीमावर्ती किसानों के लिए भी एक अहम मंडी है, "
            "खासकर लहसुन और धनिया की फसल के लिए।",
            "ध्यान दें: यदि सुबह के समय अभी तक उस दिन का डेटा अपडेट नहीं हुआ है, तो टेबल कुछ देर बाद "
            "फिर से देखें — एगमार्कनेट दिन में आवक के साथ डेटा अपडेट करता रहता है।",
        ],
    },
    {
        "slug": "merta-mandi-bhav",
        "keyword": "merta mandi bhav",
        "h1": "मेड़ता मंडी भाव — Merta Mandi Bhav",
        "title": "मेड़ता मंडी भाव आज | Merta Mandi Bhav Today",
        "meta_description": "मेड़ता मंडी (राजस्थान) का आज का भाव — जीरा, इसबगोल, मेथी, सरसों के लाइव रेट। Merta mandi bhav, daily updated.",
        "state": "Rajasthan",
        "district": "Nagaur",
        "market": "Merta City",
        "intro": (
            "मेड़ता सिटी (नागौर, राजस्थान) जीरा और इसबगोल की मंडी के रूप में जाना जाता है। यह पेज मेड़ता "
            "मंडी का आज का भाव सीधे सरकारी डेटा से लाइव दिखाता है।"
        ),
        "body_paras": [
            "जीरा और इसबगोल जैसी मसाला फसलों का भाव मौसम और निर्यात मांग से काफ़ी प्रभावित होता है, "
            "इसलिए मेड़ता मंडी का रेट अक्सर तेज़ी-मंदी के साथ बदलता रहता है।",
            "नीचे टेबल में मेड़ता मंडी की सभी उपलब्ध फसलों का न्यूनतम, अधिकतम और मोडल भाव दिखाया गया है।",
        ],
    },
    {
        "slug": "harda-mandi-bhav",
        "keyword": "harda mandi bhav",
        "h1": "हरदा मंडी भाव — Harda Mandi Bhav",
        "title": "हरदा मंडी भाव आज | Harda Mandi Bhav Today",
        "meta_description": "हरदा मंडी (मध्य प्रदेश) का आज का भाव — सोयाबीन, गेहूं, चना के लाइव रेट। Harda mandi bhav today, daily updated.",
        "state": "Madhya Pradesh",
        "district": "Harda",
        "market": "Harda",
        "intro": (
            "हरदा मध्य प्रदेश की एक प्रमुख सोयाबीन मंडी है। यह पेज हरदा मंडी का आज का भाव सीधे "
            "एगमार्कनेट से लाइव दिखाता है।"
        ),
        "body_paras": [
            "हरदा क्षेत्र में सोयाबीन और गेहूं की खेती बड़े स्तर पर होती है, जिससे यहाँ का मंडी भाव "
            "क्षेत्र के किसानों के लिए सीधा आर्थिक असर रखता है।",
            "टेबल में दिख रहे आँकड़े रुपये प्रति क्विंटल में हैं और हर पेज-लोड पर ताज़ा डेटा लाया जाता है।",
        ],
    },
    {
        "slug": "today-neemuch-mandi-bhav",
        "keyword": "today neemuch mandi bhav",
        "h1": "Today Neemuch Mandi Bhav — नीमच मंडी का आज का भाव",
        "title": "Today Neemuch Mandi Bhav | नीमच मंडी आज का भाव",
        "meta_description": "Today Neemuch mandi bhav — live garlic, soybean, gram and coriander rates from Neemuch mandi, Madhya Pradesh. Updated daily.",
        "state": "Madhya Pradesh",
        "district": "Neemuch",
        "market": "Neemuch",
        "intro": (
            "Looking for today's Neemuch mandi bhav? यह पेज नीमच मंडी का आज का लाइव भाव दिखाता है, "
            "जो सीधे data.gov.in के Agmarknet API से लिया जाता है — कोई पुराना या सेव किया हुआ डेटा नहीं।"
        ),
        "body_paras": [
            "लहसुन (garlic) की क़ीमत के मामले में नीमच देश की प्रमुख मंडियों में आता है, और यहाँ का "
            "रोज़ का भाव दूसरी मंडियों के व्यापारियों के लिए भी एक संकेत होता है।",
            "अगर टेबल में आज की तारीख़ का डेटा नहीं दिख रहा, तो थोड़ी देर बाद रीफ़्रेश करें — सुबह के "
            "शुरुआती घंटों में कभी-कभी डेटा अपडेट होने में समय लगता है।",
        ],
    },
    {
        "slug": "kota-mandi-bhav-today",
        "keyword": "kota mandi bhav today",
        "h1": "कोटा मंडी भाव आज — Kota Mandi Bhav Today",
        "title": "कोटा मंडी भाव आज | Kota Mandi Bhav Today",
        "meta_description": "कोटा मंडी (राजस्थान) का आज का भाव — धनिया, सोयाबीन, गेहूं के लाइव रेट। Kota mandi bhav today, daily updated from Agmarknet.",
        "state": "Rajasthan",
        "district": "Kota",
        "market": "Kota",
        "intro": (
            "कोटा राजस्थान की धनिया मंडी के रूप में मशहूर है। यह पेज कोटा मंडी का आज का भाव सीधे "
            "एगमार्कनेट से लाइव दिखाता है।"
        ),
        "body_paras": [
            "धनिया के अलावा कोटा मंडी में सोयाबीन और गेहूं की भी अच्छी आवक रहती है। कोटा का धनिया रेट "
            "अक्सर पूरे हाड़ौती क्षेत्र के लिए बेंचमार्क माना जाता है।",
            "नीचे टेबल में आज की उपलब्ध फसलों के भाव रुपये प्रति क्विंटल में दिए गए हैं।",
        ],
    },
    {
        "slug": "mandi-ka-bhav",
        "keyword": "mandi ka bhav",
        "h1": "मंडी का भाव — Mandi Ka Bhav (Live)",
        "title": "मंडी का भाव आज | Mandi Ka Bhav Live",
        "meta_description": "मंडी का भाव लाइव देखें — अपनी मंडी और फसल चुनकर आज का सही रेट जानें। Mandi ka bhav, updated daily from official Agmarknet data.",
        "state": "",
        "district": "",
        "market": "",
        "search_default": True,
        "intro": (
            "\"मंडी का भाव\" जानना हर किसान और व्यापारी की रोज़ की ज़रूरत है। इस पेज पर आप किसी भी "
            "मंडी का नाम खोजकर आज का लाइव भाव देख सकते हैं — बिना किसी पुराने या अंदाज़े वाले आँकड़े के।"
        ),
        "body_paras": [
            "मंडी का भाव तय करने में सबसे बड़ा रोल आवक (कितना माल मंडी में आया) और मांग का होता है। "
            "ज़्यादा आवक होने पर भाव में नरमी आ सकती है, और कम आवक में तेज़ी देखी जाती है।",
            "यह डेटा भारत सरकार के एगमार्कनेट पोर्टल से सीधे लिया गया है। पेज पर कोई डेटा सेव नहीं होता "
            "— हर विज़िट पर ताज़ा जानकारी लाई जाती है।",
        ],
    },
]

HOME_PAGE = {
    "slug": "index",
    "keyword": "mandi bhav today live",
    "h1": "मंडी भाव — सभी प्रमुख मंडियों का आज का रेट",
    "title": "मंडी भाव लाइव | MandiBhavToday — Neemuch, Indore, Kota, Merta, Harda",
    "meta_description": "नीमच, इंदौर, मेड़ता, हरदा, कोटा मंडी का आज का भाव एक जगह — लाइव डेटा, हर दिन अपडेट, सीधे Agmarknet से।",
    "state": "",
    "district": "",
    "market": "",
    "search_default": True,
    "intro": (
        "एक जगह पर कई मंडियों का भाव देखें। नीचे खोज बॉक्स में मंडी का नाम लिखें, या ऊपर मेन्यू से "
        "सीधे अपनी मंडी के पेज पर जाएँ — नीमच, इंदौर, मेड़ता, हरदा और कोटा।"
    ),
    "body_paras": [
        "MandiBhavToday हर मंडी पेज पर लाइव डेटा सीधे भारत सरकार के Agmarknet (data.gov.in) पोर्टल से "
        "दिखाता है। कोई भी रेट यहाँ सेव नहीं किया जाता — हर बार पेज खोलने पर ताज़ा जानकारी लाई जाती है।",
        "अपनी पसंदीदा मंडी जल्दी खोजने के लिए ऊपर मेन्यू में दिए गए शहरों पर क्लिक करें, या नीचे टेबल "
        "में सीधे मंडी/फसल का नाम सर्च करें।",
    ],
}

RELATED_LINKS_POOL = [
    ("neemuch-mandi-bhav.html", "नीमच मंडी भाव"),
    ("indore-mandi-bhav.html", "इंदौर मंडी भाव"),
    ("mandi-bhav-today.html", "आज का मंडी भाव"),
    ("mandi-bhav.html", "मंडी भाव"),
    ("neemuch-mandi-bhav-today.html", "नीमच मंडी भाव आज"),
    ("merta-mandi-bhav.html", "मेड़ता मंडी भाव"),
    ("harda-mandi-bhav.html", "हरदा मंडी भाव"),
    ("today-neemuch-mandi-bhav.html", "Today नीमच मंडी भाव"),
    ("kota-mandi-bhav-today.html", "कोटा मंडी भाव आज"),
    ("mandi-ka-bhav.html", "मंडी का भाव"),
]


def render_nav(current_slug):
    items = []
    for href, label in NAV_LINKS:
        active = " active" if href == f"{current_slug}.html" else ""
        items.append(f'<a href="{href}" class="{active.strip()}">{label}</a>')
    return "\n        ".join(items)


def render_related(current_slug):
    links = [
        (href, label)
        for href, label in RELATED_LINKS_POOL
        if href != f"{current_slug}.html"
    ][:6]
    return "\n          ".join(
        f'<a href="{href}">{label} देखें →</a>' for href, label in links
    )


def render_search_box(page):
    if page.get("search_default"):
        return """
        <input
          type="text"
          id="mandiSearchInput"
          class="mandi-search"
          placeholder="मंडी का नाम लिखें — जैसे Neemuch, Indore, Kota"
          autocomplete="off"
        />"""
    return ""


def render_filter_script(page):
    """Either a fixed market filter or a free-text search against all-India data."""
    if page.get("search_default"):
        return """
    <script>
      let allRecordsCache = [];

      async function boot() {
        document.querySelectorAll("[data-mandi-date-stamp]").forEach(
          (el) => (el.textContent = todayStampText())
        );
        try {
          allRecordsCache = await fetchMandiBhav({ limit: 500 });
          const latest = latestDateOnly(allRecordsCache);
          allRecordsCache = latest;
          renderMandiTable("mandiTableBody", latest);
          const countEl = document.querySelector("[data-mandi-row-count]");
          if (countEl) countEl.textContent = String(latest.length);
        } catch (err) {
          renderError("mandiTableBody", err);
        }
      }

      function wireSearch() {
        const input = document.getElementById("mandiSearchInput");
        if (!input) return;
        input.addEventListener("input", () => {
          const q = input.value.trim().toLowerCase();
          if (!q) {
            renderMandiTable("mandiTableBody", allRecordsCache);
            return;
          }
          const filtered = allRecordsCache.filter((r) =>
            [r.market, r.district, r.commodity, r.state]
              .filter(Boolean)
              .some((v) => String(v).toLowerCase().includes(q))
          );
          renderMandiTable("mandiTableBody", filtered);
        });
      }

      boot();
      wireSearch();
    </script>"""
    else:
        filt = {
            k: v
            for k, v in {
                "state": page.get("state"),
                "district": page.get("district"),
                "market": page.get("market"),
            }.items()
            if v
        }
        filt_js = ", ".join(f'{k}: "{v}"' for k, v in filt.items())
        return f"""
    <script>
      initMandiPage({{ {filt_js} }});
    </script>"""


PAGE_TEMPLATE = """<!doctype html>
<html lang="hi">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{meta_description}" />
<link rel="canonical" href="{base_url}/{slug}.html" />

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{meta_description}" />
<meta property="og:url" content="{base_url}/{slug}.html" />
<meta property="og:locale" content="hi_IN" />

<!-- Twitter -->
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{meta_description}" />

<!-- Structured data -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{title}",
  "description": "{meta_description}",
  "url": "{base_url}/{slug}.html",
  "inLanguage": "hi",
  "isPartOf": {{
    "@type": "WebSite",
    "name": "{site_name}",
    "url": "{base_url}/"
  }}
}}
</script>

<!-- Bootstrap (layout utilities only; visual system overridden by mandi-theme.css) -->
<link
  href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/css/bootstrap.min.css"
  rel="stylesheet"
/>
<link rel="stylesheet" href="mandi-theme.css" />
</head>
<body>

<header class="mandi-masthead">
  <div class="mandi-masthead-inner">
    <p class="mandi-wordmark">Mandi<span>Bhav</span>Today</p>
    <p class="mandi-tagline">रोज़ का ताज़ा भाव · सीधे एगमार्कनेट से</p>
  </div>
  <nav class="mandi-nav">
    <div class="mandi-nav-inner">
        {nav}
    </div>
  </nav>
</header>

<section class="mandi-hero">
  <div>
    <h1>{h1}</h1>
    <p class="lede">{intro}</p>
  </div>
  <div class="mandi-stamp">
    <span class="mandi-stamp-label">आज की तारीख़</span>
    <span class="mandi-stamp-date" data-mandi-date-stamp>—</span>
  </div>
</section>

<div class="mandi-toolbar">
  <p class="mandi-meta"><strong data-mandi-row-count>—</strong> फसलों का रेट दिखाया जा रहा है</p>
  {search_box}
</div>

<div class="mandi-table-wrap">
  <table class="mandi-table">
    <caption>स्रोत: Agmarknet / data.gov.in — Variety-wise Daily Market Prices · भाव ₹ प्रति क्विंटल में</caption>
    <thead>
      <tr>
        <th>फसल (Commodity)</th>
        <th>किस्म (Variety)</th>
        <th>मंडी (Market)</th>
        <th>न्यूनतम (Min)</th>
        <th>अधिकतम (Max)</th>
        <th>मोडल (Modal)</th>
      </tr>
    </thead>
    <tbody id="mandiTableBody">
      <tr class="mandi-loading-row"><td colspan="6">&nbsp;</td></tr>
      <tr class="mandi-loading-row"><td colspan="6">&nbsp;</td></tr>
      <tr class="mandi-loading-row"><td colspan="6">&nbsp;</td></tr>
    </tbody>
  </table>
</div>

<article class="mandi-article">
  <div>
    <h2>{h1}</h2>
    {body_paras_html}
  </div>
  <aside class="mandi-aside">
    <h3>अन्य मंडी भाव देखें</h3>
    {related_links}
  </aside>
</article>

<footer class="mandi-footer">
  <div class="mandi-footer-inner">
    डेटा स्रोत: <a href="https://agmarknet.gov.in/" target="_blank" rel="noopener">Agmarknet</a> /
    <a href="https://www.data.gov.in/" target="_blank" rel="noopener">data.gov.in</a> — भारत सरकार,
    कृषि एवं किसान कल्याण मंत्रालय। यह पेज जानकारी के लिए है; वास्तविक बिक्री से पहले अपनी नज़दीकी
    मंडी में भाव की पुष्टि अवश्य करें। डेटा यहाँ सेव नहीं किया जाता — हर पेज-लोड पर लाइव लाया जाता है।
  </div>
</footer>

<script src="mandi-data.js"></script>
{filter_script}

</body>
</html>
"""


def render_body_paras(paras):
    return "\n    ".join(f"<p>{p}</p>" for p in paras)


def build():
    os.makedirs(OUT_DIR, exist_ok=True)
    for page in PAGES + [HOME_PAGE]:
        html = PAGE_TEMPLATE.format(
            title=page["title"],
            meta_description=page["meta_description"],
            base_url=BASE_URL,
            slug=page["slug"],
            site_name=SITE_NAME,
            nav=render_nav(page["slug"]),
            h1=page["h1"],
            intro=page["intro"],
            search_box=render_search_box(page),
            body_paras_html=render_body_paras(page["body_paras"]),
            related_links=render_related(page["slug"]),
            filter_script=render_filter_script(page),
        )
        out_path = os.path.join(OUT_DIR, f"{page['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"wrote {out_path}")


if __name__ == "__main__":
    build()
