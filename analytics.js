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
    if (href.indexOf("chaos-keeper-hub.lovable.app") !== -1) return "chaos_keeper_demo_click";
    if (href.indexOf("sarah-sparks-ops-hub.lovable.app") !== -1) return "ops_hub_click";
    if (href.indexOf("assets/") === 0) return "asset_click";
    if (href.indexOf("resume.html") !== -1) return "resume_page_click";
    if (href.indexOf("presentation.html") !== -1) return "crm_case_study_click";
    if (href.indexOf("customer-success-portfolio.html") !== -1) return "customer_success_click";
    if (href.indexOf("dragon-hoard-tracker.html") !== -1) return "dragon_hoard_project_click";
    if (href.indexOf("index.html") !== -1) return "home_click";
    if (href.indexOf("http") === 0) return "outbound_click";

    return text ? "link_click" : null;
  }

  document.addEventListener("click", function (event) {
    var link = event.target.closest && event.target.closest("a[href]");
    if (!link) return;

    var eventName = getLinkCategory(link);
    if (!eventName) return;

    sendEvent(eventName, {
      link_url: link.href,
      link_text: (link.textContent || "").trim().replace(/\s+/g, " "),
      page_path: window.location.pathname,
    });
  });
})();
