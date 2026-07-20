(function () {
  function sendEvent(name, params) {
    if (typeof window.gtag !== "function") return;
    window.gtag("event", name, params);
  }
  function getLinkCategory(link) {
    var href = link.getAttribute("href") || "";
    var text = (link.textContent || "").trim().replace(/\s+/g, " ");
    if (href.indexOf("mailto:") === 0) return "email_click";
    if (href.indexOf("linkedin.com") !== -1) return "linkedin_click";
    if (href.indexOf("resume-crypt.onrender.com") !== -1) return "resume_crypt_live_click";
    if (href.indexOf("organizedchaosops.com") !== -1) return "about_click";
    if (href.indexOf("assets/") === 0) return "asset_click";
    if (href.indexOf("phantom-inbox.html") !== -1) return "inbox_warden_click";
    if (href.indexOf("resume-crypt.html") !== -1) return "resume_crypt_case_study_click";
    if (href.indexOf("local-ai-infrastructure.html") !== -1) return "local_ai_click";
    if (href.indexOf("customer-success-portfolio.html") !== -1) return "crm_case_study_click";
    if (href.indexOf("death-care-data.html") !== -1) return "death_care_data_click";
    if (href.indexOf("dragon-hoard-tracker.html") !== -1) return "dragon_hoard_click";
    if (href.indexOf("resume.html") !== -1) return "resume_page_click";
    if (href.indexOf("index.html") !== -1) return "home_click";
    if (href.indexOf("http") === 0) return "outbound_click";
    return text ? "link_click" : null;
  }
  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest("a[href]");
    if (!link) return;
    var eventName = getLinkCategory(link);
    if (!eventName) return;
    sendEvent(eventName, { link_url: link.href, link_text: (link.textContent || "").trim().replace(/\s+/g, " "), page_path: window.location.pathname });
  });
})();