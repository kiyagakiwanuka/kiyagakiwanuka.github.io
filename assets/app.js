/* Tabs + project modal. Without JS, tabs stack and cards link to standalone pages. */
(function(){
  var d=document, panels=[].slice.call(d.querySelectorAll('.panel')), ids=panels.map(function(p){return p.dataset.tab}),
      cur='about', modal=d.getElementById('pm'), box=modal.querySelector('.pm-body'), lastFocus=null, cache={};
  d.documentElement.classList.add('js');
  function setTab(h){ cur=h; panels.forEach(function(p){p.classList.toggle('active',p.dataset.tab===h)});
    d.querySelectorAll('#tabs a').forEach(function(a){a.classList.toggle('on',a.getAttribute('href').split('#')[1]===h)}); }
  function cardFor(slug){ return d.querySelector('.card[data-slug="'+slug+'"]'); }
  function route(){
    var h=decodeURIComponent(location.hash.slice(1));
    if(h.indexOf('project=')===0){ var c=cardFor(h.slice(8)); if(c){ setTab(c.closest('.panel').dataset.tab); open(c,false); return; } h=''; }
    if(modal.classList.contains('open')) close(false);
    setTab(ids.indexOf(h)<0?'about':h); window.scrollTo(0,0);
  }
  function abs(base,html){ var t=d.createElement('div'); t.innerHTML=html;
    t.querySelectorAll('[src],[href]').forEach(function(el){ ['src','href'].forEach(function(k){ var v=el.getAttribute(k);
      if(v && !/^(https?:|mailto:|#)/.test(v)) el.setAttribute(k,new URL(v,base).href); }); });
    t.querySelectorAll('.toc a').forEach(function(a){ var id=a.getAttribute('href').split('#')[1]; a.setAttribute('href','#'); a.dataset.jump=id; });
    t.querySelectorAll('[id]').forEach(function(el){ el.id='pm-'+el.id; });
    var back=t.querySelector('.back'); if(back) back.remove(); return t.innerHTML; }
  function open(card,push){
    lastFocus=card; var url=new URL(card.getAttribute('href'),location.href).href;
    box.innerHTML='<p class="pm-loading">Loading…</p>'; modal.classList.add('open'); modal.setAttribute('aria-hidden','false');
    d.body.classList.add('noscroll'); modal.querySelector('.pm-close').focus();
    if(push) history.pushState(null,'','#project='+card.dataset.slug);
    var done=function(html){ var doc=new DOMParser().parseFromString(html,'text/html');
      var hero=doc.querySelector('.hero'), art=doc.querySelector('article');
      box.innerHTML=abs(url,(hero?'<header class="pm-hero">'+hero.querySelector('.wrap').innerHTML+'</header>':'')+(art?art.innerHTML:''));
      var h1=box.querySelector('h1'); if(h1){h1.id='pm-title'}; box.scrollTop=0;
      box.insertAdjacentHTML('beforeend','<p class="pm-full"><a href="'+url+'">Open as full page ↗</a></p>'); };
    if(cache[url]) return done(cache[url]);
    fetch(url).then(function(r){return r.text()}).then(function(t){cache[url]=t;done(t)}).catch(function(){location.href=url});
  }
  function close(push){ modal.classList.remove('open'); modal.setAttribute('aria-hidden','true'); d.body.classList.remove('noscroll');
    if(push!==false) history.replaceState(null,'','#'+cur); if(lastFocus) lastFocus.focus(); }
  d.addEventListener('click',function(e){
    var c=e.target.closest('.card[data-slug]');
    if(c && !e.ctrlKey && !e.metaKey && !e.shiftKey && e.button===0){ e.preventDefault(); open(c,true); return; }
    var j=e.target.closest('[data-jump]'); if(j){ e.preventDefault(); var t=d.getElementById('pm-'+j.dataset.jump); if(t) box.scrollTo({top:t.offsetTop-box.offsetTop-10,behavior:'smooth'}); }
  });
  modal.querySelector('.pm-close').addEventListener('click',function(){close()});
  modal.querySelector('.pm-backdrop').addEventListener('click',function(){close()});
  d.addEventListener('keydown',function(e){ if(!modal.classList.contains('open')) return;
    if(e.key==='Escape'){ close(); return; }
    if(e.key==='Tab'){ var f=[].slice.call(modal.querySelectorAll('a[href],button,[tabindex]:not([tabindex="-1"])')); if(!f.length) return;
      var a=f[0], z=f[f.length-1]; if(e.shiftKey && d.activeElement===a){e.preventDefault();z.focus()} else if(!e.shiftKey && d.activeElement===z){e.preventDefault();a.focus()} } });
  window.addEventListener('hashchange',route); route();
})();
