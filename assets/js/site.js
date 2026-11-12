(() => {
  'use strict';

  const activities = [
    { id:'favor', cls:'E', name:'Favores de NPC', subtitle:'Encargos breves', cops:'0', cap:'Según encargo', state:'Disponible con ficha', rule:'No requiere solicitud por /robos. El encargo indica el objetivo, el resultado y si corresponde /entorno. No tiene mínimo policial general.', note:'Los detalles concretos del favor se publican en su ficha.' },
    { id:'drug-sale', cls:'E', name:'Venta de droga a NPC', subtitle:'Actividad de calle', cops:'1', cap:'Sin cifra común', state:'Disponible con ficha', rule:'Aviso automático en el primer intento de venta de la sesión y un /entorno al comenzar, indicando personas y vehículo si lo hay. No se envía un entorno por transacción.', note:'El mínimo policial bloquea el inicio cuando no se cumple.' },
    { id:'wood', cls:'E', name:'Recogida de madera', subtitle:'Palés', cops:'1', cap:'Según actividad', state:'Disponible con ficha', rule:'Aviso automático por cada palé y /entorno antes de empezar. No requiere solicitud por /robos.', note:'Respeta el límite y el objeto que marque su ficha.' },
    { id:'wheels', cls:'E', name:'Robo de ruedas', subtitle:'Por vehículo', cops:'1', cap:'Según ficha', state:'Disponible con ficha', rule:'No genera aviso automático. Envía /entorno antes de retirar la primera rueda de cada vehículo.', note:'No se ha fijado un máximo general de participantes.' },
    { id:'tombs', cls:'D', name:'Robo de tumbas', subtitle:'Delito local', cops:'1', cap:'Según ficha', state:'Disponible con ficha', rule:'Aviso automático al producirse el robo. No exige /entorno. Puedes abandonar el lugar al terminar.', note:'El mínimo policial se comprueba antes de empezar.' },
    { id:'atm', cls:'D', name:'Cajeros automáticos', subtitle:'Manipulación del cajero', cops:'1', cap:'Según ficha', state:'Disponible con ficha', rule:'Aviso automático al empezar a manipular el cajero. No exige /entorno. Puedes abandonar el lugar al terminar.', note:'El mínimo policial se comprueba antes de empezar.' },
    { id:'meter', cls:'D', name:'Parquímetros', subtitle:'Delito local', cops:'1', cap:'Según ficha', state:'Disponible con ficha', rule:'Aviso automático al robar el parquímetro. No exige /entorno. Puedes marcharte al terminar.', note:'El mínimo policial se comprueba antes de empezar.' },
    { id:'import', cls:'D', name:'Importación de vehículos', subtitle:'Contrato y entrega', cops:'1', cap:'Según contrato', state:'Disponible con ficha', rule:'Se acepta con el contacto correspondiente, no por /robos. Al salir con el vehículo objetivo se activa el aviso policial y un localizador de 5 minutos. No hay negociación ni espera obligatoria: completa la entrega dentro del tiempo del contrato.', note:'El procedimiento no depende de las coordenadas publicadas en esta guía.' },
    { id:'shops', cls:'D', name:'Tiendas y comercios', subtitle:'24/7 · LTD · licorería · peluquería · tatuajes · librería · ropa', cops:'2', cap:'Máx. 2 robando', state:'Disponible con ficha', rule:'Sin rehenes, apoyo exterior, conductor dedicado, bloqueos, tiroteos ni negociación. El establecimiento envía su aviso; /entorno antes de empezar, con personas y vehículo. Registradoras y caja fuerte opcional son una misma actividad.', note:'Si la policía no llega, puedes marcharte 5 minutos después de terminar. Si llega, puede intervenir. LTD comparte clasificación y cupo con el grupo 24/7.' },
    { id:'houses', cls:'D', name:'Robo de casas · nivel 1', subtitle:'Los niveles superiores requieren ficha propia', cops:'1', cap:'Según ficha', state:'Parámetros parciales', rule:'El primer nivel exige un mínimo de 1 policía. Avisos, entorno, aforo y salida se rigen por la ficha publicada de ese nivel. Los niveles superiores no se deben inferir.', note:'No inicies niveles superiores sin una ficha completa publicada.' },
    { id:'scrapyard', cls:'C', name:'Desguace', subtitle:'Robo coordinado', cops:'2', cap:'2 robando · 3 total', state:'Disponible con ficha', rule:'Aceptación previa por /robos y /entorno antes de empezar. Máximo 2 rehenes. Al completar, espera a la policía; con rehenes se negocia la salida, sin ellos la policía puede intervenir.', note:'Quien conduzca, vigile o apoye cuenta dentro del máximo total.' },
    { id:'pawnshop', cls:'C', name:'Pawnshop · tienda de empeño', subtitle:'Robo coordinado', cops:'3', cap:'3 robando · 4 total', state:'Disponible con ficha', rule:'Aceptación previa por /robos y /entorno antes de empezar. Máximo 2 rehenes. El dependiente representado en rol cuenta si se usa como rehén. Al completar, espera la llegada policial.', note:'Quien conduzca, vigile o apoye cuenta dentro del máximo total.' },
    { id:'fleeca', cls:'B', name:'Fleeca', subtitle:'Banco', cops:'4', cap:'2–3 robando · 5 total', state:'Disponible con ficha', rule:'Aceptación previa por /robos y /entorno antes de empezar. Máximo 4 rehenes. El recepcionista cuenta solo si se utiliza como rehén. Al completar, permanece dentro hasta que llegue la policía.', note:'La negociación no tiene un límite global de duración.' },
    { id:'jewelry', cls:'B', name:'Joyería', subtitle:'Robo de alto riesgo', cops:'5', cap:'2–4 robando · 6 total', state:'Disponible con ficha', rule:'Aceptación previa por /robos y /entorno antes de empezar. Hasta 4 rehenes reales; dependientes y NPC no cuentan. Al completar, espera dentro la llegada policial y negocia si hay rehenes.', note:'La negociación no tiene un límite global de duración.' },
    { id:'ammu', cls:'B', name:'Ammu-Nation', subtitle:'Armería', cops:'5', cap:'2–4 robando · 6 total', state:'Disponible con ficha', rule:'Mismo aforo y procedimiento que joyería: aceptación previa por /robos, /entorno antes de empezar, máximo 4 rehenes reales y espera dentro a la policía.', note:'Dependientes y NPC no cuentan como rehenes.' },
    { id:'paleto', cls:'A', name:'Banco Paleto', subtitle:'Operación mayor', cops:'6', cap:'2–4 robando · 8 total', state:'Disponible con ficha', rule:'Aceptación previa por /robos y /entorno antes de empezar. Máximo 6 rehenes. Al completar, espera la evolución de la escena policial; la negociación o intervención dependen del contexto.', note:'La cifra pública mínima de recompensa aprobada para el grupo es 60.000 de dinero negro; otros valores pueden cambiar.' },
    { id:'sandy-bank', cls:'A', name:'Banco de Sandy', subtitle:'Operación mayor', cops:'6', cap:'2–4 robando · 8 total', state:'Disponible con ficha', rule:'Mismas cifras y procedimiento que Banco Paleto: aceptación por /robos, /entorno antes de empezar y máximo 6 rehenes.', note:'Quien conduzca, vigile o apoye cuenta dentro del máximo total.' },
    { id:'armored-van', cls:'A', name:'Furgón blindado grande', subtitle:'Ficha incompleta', cops:'Pendiente', cap:'Pendiente', state:'No disponible', pending:true, rule:'La actividad está clasificada como A, pero faltan por publicar sus mínimos, aforos, avisos y procedimiento. No se puede iniciar hasta completar la ficha.', note:'No se deben deducir condiciones de otra actividad.' },
    { id:'train', cls:'S', name:'Tren de mercancías', subtitle:'Ficha completa pendiente', cops:'Pendiente', cap:'Pendiente', state:'No disponible', pending:true, rule:'Actividad S. No está habilitada hasta que se publique una ficha completa con mínimos, aforos, avisos, armas, procedimiento y límites.', note:'No se publican detalles internos de recompensa o materiales.' },
    { id:'humane', cls:'S', name:'Humane Labs', subtitle:'Ficha pendiente', cops:'Pendiente', cap:'Pendiente', state:'No disponible', pending:true, rule:'Actividad S. No está habilitada hasta la publicación de su ficha completa.', note:'Los requisitos no se deben asumir.' },
    { id:'casino', cls:'S+', name:'Diamond Casino', subtitle:'Ficha pendiente', cops:'Pendiente', cap:'Pendiente', state:'No disponible', pending:true, rule:'Actividad S+. No está habilitada hasta la publicación de su ficha completa.', note:'Los requisitos no se deben asumir.' },
    { id:'central-bank', cls:'S+', name:'Banco Central', subtitle:'Ficha pendiente', cops:'Pendiente', cap:'Pendiente', state:'No disponible', pending:true, rule:'Actividad S+. No está habilitada hasta la publicación de su ficha completa.', note:'Los requisitos no se deben asumir.' }
  ];

  const normalize = value => value.toLocaleLowerCase('es').normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  const body = document.body;
  const activityBody = document.querySelector('#activity-list');
  const searchInput = document.querySelector('#activity-search');
  const noResults = document.querySelector('#no-results');
  let activeFilter = 'all';
  let query = '';

  const esc = value => String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  function renderActivities() {
    if (!activityBody) return;
    const found = activities.filter(item => (activeFilter === 'all' || item.cls === activeFilter) && (!query || normalize(`${item.name} ${item.subtitle} ${item.cls}`).includes(normalize(query))));
    activityBody.innerHTML = found.map(item => {
      const buttonId = `detail-${item.id}`;
      const status = item.pending ? 'pending' : '';
      return `<tr class="activity-row" data-id="${item.id}">
        <td><div class="activity-name"><span class="class-pill ${item.pending?'class-pending':''}">${esc(item.cls)}</span><span><b>${esc(item.name)}</b><small>${esc(item.subtitle)}</small></span></div></td>
        <td data-label="Policía mínima">${esc(item.cops)}${item.cops==='Pendiente'?'':' de servicio'}</td>
        <td data-label="Aforo">${esc(item.cap)}</td>
        <td data-label="Estado"><span class="activity-status ${status}">${esc(item.state)}</span></td>
        <td><button class="details-toggle" type="button" aria-expanded="false" aria-controls="${buttonId}" aria-label="Ver detalles de ${esc(item.name)}">+</button></td>
      </tr><tr class="activity-detail-row" id="${buttonId}" hidden><td colspan="5"><div class="activity-detail"><div class="activity-detail-head"><span>${esc(item.cls)} / ${esc(item.name)}</span><span class="activity-detail-label">${item.pending?'FICHA PENDIENTE':'MARCO PÚBLICO'}</span></div><p>${esc(item.rule)}</p><span class="activity-detail-note">${esc(item.note)}</span></div></td></tr>`;
    }).join('');
    noResults.hidden = found.length > 0;
  }
  renderActivities();

  document.querySelectorAll('.filter-chip').forEach(button => button.addEventListener('click', () => {
    activeFilter = button.dataset.filter;
    document.querySelectorAll('.filter-chip').forEach(chip => {const selected = chip === button; chip.classList.toggle('is-active', selected); chip.setAttribute('aria-pressed', String(selected));});
    renderActivities();
  }));
  searchInput?.addEventListener('input', () => {query = searchInput.value; renderActivities();});
  document.addEventListener('click', event => {
    const toggle = event.target.closest('.details-toggle');
    if (!toggle) return;
    const row = document.getElementById(toggle.getAttribute('aria-controls'));
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    row.hidden = !open;
    if (open) row.querySelector('.activity-detail').setAttribute('tabindex','-1');
  });
  document.addEventListener('keydown', event => {
    if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey) return;
    if (/input|textarea|select/i.test(document.activeElement?.tagName || '') || document.activeElement?.isContentEditable) return;
    if (window.location.hash === '#actividades' || document.querySelector('#actividades')?.getBoundingClientRect().top < window.innerHeight * .55) {event.preventDefault(); searchInput?.focus();}
  });

  const navToggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('#primary-nav');
  navToggle?.addEventListener('click', () => {
    const open = navToggle.getAttribute('aria-expanded') !== 'true';
    navToggle.setAttribute('aria-expanded', String(open));
    navToggle.setAttribute('aria-label', open ? 'Cerrar navegación' : 'Abrir navegación');
    nav.classList.toggle('is-open', open);
  });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {nav.classList.remove('is-open');navToggle?.setAttribute('aria-expanded','false');}));

  const docPanel = document.querySelector('#doc-content');
  const docTabs = [...document.querySelectorAll('.doc-switch [role="tab"]')];
  let currentDoc = '';
  const slug = text => text.toLocaleLowerCase('es').trim().replace(/[^\p{L}\p{N}\s-]/gu,'').replace(/\s+/g,'-');
  function inlineMarkdown(source) {
    let text = esc(source);
    text = text.replace(/`([^`]+)`/g,'<code>$1</code>');
    text = text.replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>').replace(/\*(.+?)\*/g,'<em>$1</em>');
    text = text.replace(/\[([^\]]+)\]\((#[^\s)]+|https:\/\/[^\s)]+)\)/g,'<a href="$2">$1</a>');
    return text;
  }
  function renderMarkdown(markdown) {
    const lines = markdown.replace(/\r/g,'').split('\n');
    const output=[];let paragraph=[];let listType='';let quote=[];let table=[];
    const flushParagraph=()=>{if(paragraph.length){output.push(`<p>${inlineMarkdown(paragraph.join(' '))}</p>`);paragraph=[];}};
    const flushList=()=>{if(listType){output.push(`</${listType}>`);listType='';}};
    const flushQuote=()=>{if(quote.length){output.push(`<blockquote><p>${inlineMarkdown(quote.join(' '))}</p></blockquote>`);quote=[];}};
    const flushTable=()=>{if(!table.length)return;const rows=table.map(row=>row.trim().replace(/^\|/,'').replace(/\|$/,'').split('|').map(cell=>cell.trim()));const filtered=rows.filter(row=>!row.every(cell=>/^:?-{3,}:?$/.test(cell)));if(filtered.length){const [head,...rest]=filtered;output.push(`<div class="doc-table-wrap"><table><thead><tr>${head.map(cell=>`<th>${inlineMarkdown(cell)}</th>`).join('')}</tr></thead><tbody>${rest.map(row=>`<tr>${head.map((_,i)=>`<td>${inlineMarkdown(row[i]||'')}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`);}table=[];};
    for(let i=0;i<lines.length;i++){
      const line=lines[i];
      if(line.trim().startsWith('|')){flushParagraph();flushList();flushQuote();table.push(line);continue;}else flushTable();
      if(!line.trim()){flushParagraph();flushList();flushQuote();continue;}
      const heading=line.match(/^(#{1,3})\s+(.+)$/);if(heading){flushParagraph();flushList();flushQuote();const level=heading[1].length;const title=heading[2].replace(/\s+#+\s*$/,'');const id=slug(title);output.push(`<h${level} id="${esc(id)}">${inlineMarkdown(title)}</h${level}>`);continue;}
      if(/^\s*---+\s*$/.test(line)){flushParagraph();flushList();flushQuote();output.push('<hr>');continue;}
      const quoted=line.match(/^>\s?(.*)$/);if(quoted){flushParagraph();flushList();quote.push(quoted[1]);continue;}else flushQuote();
      const item=line.match(/^\s*[-*]\s+(.+)$/);if(item){flushParagraph();if(listType!=='ul'){flushList();listType='ul';output.push('<ul>');}output.push(`<li>${inlineMarkdown(item[1])}</li>`);continue;}
      const numbered=line.match(/^\s*\d+\.\s+(.+)$/);if(numbered){flushParagraph();if(listType!=='ol'){flushList();listType='ol';output.push('<ol>');}output.push(`<li>${inlineMarkdown(numbered[1])}</li>`);continue;}
      flushList();paragraph.push(line.trim());
    }
    flushParagraph();flushList();flushQuote();flushTable();
    return output.join('\n');
  }
  async function loadDoc(name) {
    if(!docPanel || currentDoc===name)return;
    currentDoc=name;docPanel.innerHTML='<p class="doc-loading">Cargando documento…</p>';
    docPanel.setAttribute('aria-labelledby',name==='normativa'?'tab-normativa':'tab-guia');
    docTabs.forEach(tab=>{const selected=tab.dataset.doc===name;tab.setAttribute('aria-selected',String(selected));tab.tabIndex=selected?0:-1;});
    try{const response=await fetch(`content/${name}.md`);if(!response.ok)throw new Error('document unavailable');const markdown=await response.text();docPanel.innerHTML=renderMarkdown(markdown);}
    catch{docPanel.innerHTML='<p class="doc-loading">No se pudo cargar el documento. Abre la página desde GitHub Pages o desde un servidor local.</p>';currentDoc='';}
  }
  docTabs.forEach((tab,index)=>{
    tab.addEventListener('click',()=>loadDoc(tab.dataset.doc));
    tab.addEventListener('keydown',event=>{if(event.key==='ArrowRight'||event.key==='ArrowLeft'){event.preventDefault();const next=docTabs[(index+(event.key==='ArrowRight'?1:-1)+docTabs.length)%docTabs.length];next.focus();next.click();}});
  });
  loadDoc('normativa');

  const reveals=document.querySelectorAll('.section-kicker,.intro-grid,.system-map,.section-heading,.progress-card,.progress-note,.quota-board,.protocol-card,.rule-tile,.status-card');
  if('IntersectionObserver' in window&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('is-visible');observer.unobserve(entry.target);}}),{threshold:.08,rootMargin:'0px 0px -20px 0px'});
    reveals.forEach(element=>{element.classList.add('reveal');observer.observe(element);});
  }
  const sections=[...document.querySelectorAll('main section[id]')];
  if('IntersectionObserver' in window){const navObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){const href=`#${entry.target.id}`;nav?.querySelectorAll('a').forEach(link=>{if(link.getAttribute('href')===href)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});}}),{rootMargin:'-25% 0px -65% 0px'});sections.forEach(section=>navObserver.observe(section));}
})();
