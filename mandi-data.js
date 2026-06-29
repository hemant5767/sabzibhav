/* ==========================================================================
   mandi-data.js
   Live mandi bhav (mandi price) fetcher — calls data.gov.in / Agmarknet
   "Variety-wise Daily Market Prices Data of Commodity" API directly from
   the browser. No data is stored anywhere; every page load asks the
   government API for the latest rows.

   NOTE: This is a client-side call, so the API key below is visible to
   anyone who views the page source / network tab. That is a known and
   accepted limitation of pure HTML+JS (no backend) — see project notes.
   ========================================================================== */

const MANDI_API_KEY = "579b464db66ec23bdd0000012ee73e5c2b1d4b455f133461763f8c57";
const MANDI_RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070";
const MANDI_API_BASE = `https://api.data.gov.in/resource/${MANDI_RESOURCE_ID}`;

/**
 * Fetch latest mandi price rows for a given district / market.
 * @param {Object} opts
 * @param {string} [opts.state]    e.g. "Madhya Pradesh"
 * @param {string} [opts.district] e.g. "Neemuch"
 * @param {string} [opts.market]   e.g. "Neemuch"
 * @param {number} [opts.limit]    max rows to request (API caps around 1000)
 */
async function fetchMandiBhav({ state, district, market, limit = 100 } = {}) {
  const params = new URLSearchParams();
  params.set("api-key", MANDI_API_KEY);
  params.set("format", "json");
  params.set("limit", String(limit));
  // Sort by arrival date, newest first, where the API supports it
  params.set("sort[arrival_date]", "desc");

  if (state) params.set("filters[state.keyword]", state);
  if (district) params.set("filters[district.keyword]", district);
  if (market) params.set("filters[market.keyword]", market);

  const url = `${MANDI_API_BASE}?${params.toString()}`;

  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Mandi API request failed: ${res.status}`);
  }
  const json = await res.json();
  return Array.isArray(json.records) ? json.records : [];
}

/**
 * Pick only the most recent date present in a record set and return
 * just those rows (the API sometimes mixes a few recent dates together).
 */
function latestDateOnly(records) {
  if (!records.length) return records;
  const dates = records
    .map((r) => r.arrival_date)
    .filter(Boolean)
    .sort()
    .reverse();
  const latest = dates[0];
  return records.filter((r) => r.arrival_date === latest);
}

function escapeHtml(str) {
  return String(str ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function formatRupee(value) {
  const n = Number(value);
  if (Number.isNaN(n)) return "—";
  return "₹" + n.toLocaleString("en-IN");
}

function todayStampText() {
  const d = new Date();
  return d.toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}

/**
 * Render the price table into a container element.
 * @param {string} containerId  id of the <tbody> to fill
 * @param {Array}  records
 */
function renderMandiTable(containerId, records) {
  const tbody = document.getElementById(containerId);
  if (!tbody) return;

  if (!records.length) {
    tbody.innerHTML = `
      <tr>
        <td colspan="6" class="mandi-empty">
          आज का डेटा अभी उपलब्ध नहीं है। कुछ देर बाद फिर देखें।
          <br><span class="mandi-empty-en">No rows returned for today yet — Agmarknet usually updates through the day. Try again shortly.</span>
        </td>
      </tr>`;
    return;
  }

  tbody.innerHTML = records
    .map((r) => {
      const min = formatRupee(r.min_price);
      const max = formatRupee(r.max_price);
      const modal = formatRupee(r.modal_price);
      return `
        <tr>
          <td>${escapeHtml(r.commodity)}</td>
          <td>${escapeHtml(r.variety || "—")}</td>
          <td>${escapeHtml(r.market)}</td>
          <td class="mandi-price">${min}</td>
          <td class="mandi-price">${max}</td>
          <td class="mandi-price mandi-price-modal">${modal}</td>
        </tr>`;
    })
    .join("");
}

function renderError(containerId, err) {
  const tbody = document.getElementById(containerId);
  if (!tbody) return;
  console.error("Mandi bhav fetch error:", err);
  tbody.innerHTML = `
    <tr>
      <td colspan="6" class="mandi-empty">
        डेटा लोड करने में समस्या आई। कृपया पेज रीफ़्रेश करें।
        <br><span class="mandi-empty-en">Could not load live data right now. Please refresh the page.</span>
      </td>
    </tr>`;
}

/**
 * Boot a mandi page: fetch, filter to latest date, render, stamp the date.
 * @param {Object} filter   passed straight to fetchMandiBhav
 * @param {string} tableBodyId
 */
async function initMandiPage(filter, tableBodyId = "mandiTableBody") {
  const stampEls = document.querySelectorAll("[data-mandi-date-stamp]");
  stampEls.forEach((el) => (el.textContent = todayStampText()));

  try {
    const records = await fetchMandiBhav(filter);
    const latest = latestDateOnly(records);
    renderMandiTable(tableBodyId, latest);

    const countEl = document.querySelector("[data-mandi-row-count]");
    if (countEl) countEl.textContent = String(latest.length);

    const dateFromDataEl = document.querySelector("[data-mandi-arrival-date]");
    if (dateFromDataEl && latest[0]?.arrival_date) {
      dateFromDataEl.textContent = latest[0].arrival_date;
    }
  } catch (err) {
    renderError(tableBodyId, err);
  }
}
