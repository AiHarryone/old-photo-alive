// OldPhoto Alive — lifetime unlock (shared across all tools).
// Model: one free use per tool, then $9.99 one-time unlocks everything forever.
(function(){
  var PAY = 'https://creem.io/product/prod_6AE1xgYo8j7DIbN08Bh59S';
  var UNLOCK_API = 'https://old-photo-unlock.aiharryone.workers.dev';
  var KEY_STORE = 'oldphoto_premium';
  var USES_PREFIX = 'oldphoto_uses_';
  var LICENSE_STORE = 'oldphoto_license';

  function unlocked(){ try { return localStorage.getItem(KEY_STORE) === '1'; } catch(e){ return false; } }
  function used(tool){ try { return parseInt(localStorage.getItem(USES_PREFIX + tool), 10) || 0; } catch(e){ return 0; } }
  function markUsed(tool){ try { localStorage.setItem(USES_PREFIX + tool, String(used(tool) + 1)); } catch(e){} }
  function setUnlocked(){ try { localStorage.setItem(KEY_STORE, '1'); } catch(e){} }

  // Build + inject the paywall modal once.
  var injected = false;
  function inject(){
    if (injected) return; injected = true;
    var css = document.createElement('style');
    css.textContent = '#opModal{position:fixed;inset:0;background:rgba(40,25,10,.55);z-index:9999;display:none;align-items:center;justify-content:center;padding:20px;font-family:Helvetica,Arial,sans-serif}'
      + '#opModal.show{display:flex}'
      + '.opBox{background:#fdf6ea;border-radius:20px;max-width:420px;width:100%;padding:30px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.35);position:relative}'
      + '.opBox h2{color:#4a3420;font-family:Georgia,serif;font-size:24px;margin-bottom:8px}'
      + '.opBox .p{color:#7d6849;font-size:14px;margin-bottom:14px}'
      + '.opBox .price{font-size:38px;font-weight:bold;color:#b0703a;margin:8px 0 4px}'
      + '.opBox .once{font-size:13px;color:#9b8261}'
      + '.opBox .btn{display:block;background:linear-gradient(135deg,#c98650,#a15f2e);color:#fff;text-decoration:none;padding:14px;border-radius:999px;font-weight:bold;margin:18px 0;border:none;cursor:pointer;font-size:16px}'
      + '.opBox .keyRow{display:flex;gap:8px;margin-top:10px}'
      + '.opBox input{flex:1;padding:10px;border:2px solid #d8b98a;border-radius:10px;font-size:14px}'
      + '.opBox .unlockBtn{background:#8a7a3a;color:#fff;border:none;border-radius:10px;padding:10px 16px;font-weight:bold;cursor:pointer}'
      + '.opBox .msg{font-size:13px;color:#b04a3a;margin-top:10px;min-height:16px}'
      + '.opBox .ok{color:#6d7a2a}'
      + '.opBox .note{font-size:12px;color:#9b8261;margin-top:14px}'
      + '.opBox .x{position:absolute;top:12px;right:16px;background:none;border:none;font-size:22px;color:#9b8261;cursor:pointer}';
    document.head.appendChild(css);
    var m = document.createElement('div');
    m.id = 'opModal';
    m.innerHTML = '<div class="opBox">'
      + '<button class="x" onclick="document.getElementById(\'opModal\').classList.remove(\'show\')">×</button>'
      + '<h2>Unlock All Tools</h2>'
      + '<div class="p">You\'ve used your free try for this tool. Unlock <b>every tool on this site</b> — passport photos, background removal, PDF, GIF, watermark, scanner, restore &amp; animate — forever.</div>'
      + '<div class="price">$9.99</div><div class="once">one-time · lifetime · no subscription</div>'
      + '<a class="btn" href="' + PAY + '" target="_blank" rel="noopener">Get Lifetime Access</a>'
      + '<div class="note">Already bought? Paste your unlock code:</div>'
      + '<div class="keyRow"><input id="opKey" placeholder="e.g. ABCDE-12345" autocomplete="off"><button class="unlockBtn" id="opUnlock">Unlock</button></div>'
      + '<div class="msg" id="opMsg"></div>'
      + '</div>';
    document.body.appendChild(m);
    document.getElementById('opUnlock').onclick = function(){
      var key = document.getElementById('opKey').value.trim();
      var msg = document.getElementById('opMsg');
      if (!key) { msg.textContent = 'Paste your unlock code first.'; return; }
      msg.textContent = 'Checking…'; msg.className = 'msg';
      fetch(UNLOCK_API + '/unlock', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ key: key, instanceName: 'web-browser' }) })
        .then(function(r){ return r.json().then(function(j){ return { ok: r.ok, j: j }; }); })
        .then(function(res){
          if (res.j && (res.j.valid || res.j.ok)) {
            setUnlocked();
            try { localStorage.setItem(LICENSE_STORE, JSON.stringify({ key: key, instanceId: res.j.instanceId || '' })); } catch(e){}
            msg.textContent = 'Unlocked ✅ Enjoy every tool!'; msg.className = 'msg ok';
            setTimeout(function(){ location.reload(); }, 800);
          } else {
            msg.textContent = res.j && res.j.error ? res.j.error : 'That code did not validate.';
            msg.className = 'msg';
          }
        })
        .catch(function(){ msg.textContent = 'Could not reach the unlock service. Try again.'; });
    };
  }

  // Gate: allow if unlocked, or consume a free use; else show paywall.
  function gate(tool, maxFree, onAllow){
    if (unlocked()) { if (onAllow) onAllow(); return true; }
    if (used(tool) < maxFree) { markUsed(tool); if (onAllow) onAllow(); return true; }
    inject();
    document.getElementById('opModal').classList.add('show');
    return false;
  }

  // Reuse a stored license on load via /validate — never re-activate the same key.
  (function(){
    var lic; try { lic = JSON.parse(localStorage.getItem(LICENSE_STORE) || 'null'); } catch(e){ lic = null; }
    if (!lic || !lic.key) return;
    fetch(UNLOCK_API + '/validate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ key: lic.key, instanceId: lic.instanceId || '' }) })
      .then(function(r){ return r.json().catch(function(){ return {}; }); })
      .then(function(d){ if (d.ok){ setUnlocked(); } })
      .catch(function(){});
  })();

  window.OP = {
    unlocked: unlocked, used: used, markUsed: markUsed, gate: gate, show: function(){ inject(); document.getElementById('opModal').classList.add('show'); },
    payLink: PAY
  };
})();
