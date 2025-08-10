// posthog.js (EU, minimal, respectful)
(function (d, ph) {
  // 1) Respect Do Not Track
  var dnt = navigator.doNotTrack === '1' || window.doNotTrack === '1' || navigator.msDoNotTrack === '1';
  if (dnt) return;

  // --- PostHog loader (yours) ---
  !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture identify reset on onFeatureFlags reloadFeatureFlags getFeatureFlag getFeatureFlagPayload isFeatureEnabled getNextSurveyStep register register_once unregister".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);

  // --- 2) Init (unchanged host/key, no autocapture) ---
  posthog.init('phc_kpNVhtovGGMTUmB1sBpbPHeH0dmka0g8Lhf0BSsJOQU', {
    api_host: 'https://eu.i.posthog.com',
    autocapture: false,
    capture_pageview: true,     // keep auto pageviews
    persistence: 'localStorage' // sensible for a personal site
  });

  // --- 3) Attach UTM once (so $pageview includes them) ---
  (function registerUTMOnce() {
    var q = new URLSearchParams(location.search);
    var props = {};
    ['utm_source','utm_medium','utm_campaign','utm_term','utm_content'].forEach(function(k){
      var v = q.get(k);
      if (v) props[k] = v;
    });
    if (Object.keys(props).length) posthog.register_once(props);
  })();

  // --- 4) Optional: track on-site search (uses your #searchInput) ---
  var searchEl = document.getElementById('searchInput');
  if (searchEl) {
    var last = '';
    searchEl.addEventListener('change', function () {
      var q = (searchEl.value || '').trim();
      if (!q || q === last) return;
      last = q;
      posthog.capture('site_search', { query: q, path: location.pathname });
    });
  }

  // --- 5) Optional: outbound link clicks (simple) ---
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    try {
      var u = new URL(a.getAttribute('href'), location.href);
      if (u.origin !== location.origin) {
        posthog.capture('outbound_link_click', {
          url: u.href,
          text: (a.textContent || '').trim()
        });
      }
    } catch (_) {}
  }, { capture: true });

})(document, window.posthog);