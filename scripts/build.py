"""Genera las páginas de documentación, sin dependencias ni backend."""
from pathlib import Path
from html import escape as esc
import json
from data import MATERIALS, ROB, TABLES, RECIPES, NPC_WEAPONS, validate
from rules import INTRO, RULES

ROOT = Path(__file__).resolve().parent.parent
DATE = '12 noviembre 2026'
NAMES = {m[0]: m[1] for m in MATERIALS} | {'rueda':'Rueda', 'lockpick':'Ganzúa', 'advancedlockpick':'Ganzúa avanzada'}
PATHS = {
 'arrow':'M7 17 17 7M7 7h10v10', 'down':'m6 9 6 6 6-6', 'book':'M4 4h7l1 2 1-2h7v16h-7l-1 1-1-1H4zM12 6v15',
 'grid':'M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z',
 'tool':'m14 6 4 4M4 20l7-7m-1-5a6 6 0 0 0 7 7l4-4-5 1-4-4 1-5-4 4z',
 'people':'M16 21v-3a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v3M9 10a4 4 0 1 0 0-8 4 4 0 0 0 0 8M17 3a4 4 0 0 1 0 8m1 3a4 4 0 0 1 4 4v3',
 'box':'m3 7 9-5 9 5v10l-9 5-9-5zM3 7l9 5 9-5M12 12v10m-5-18 10 6',
 'shield':'M12 2 3 6v6c0 5 9 10 9 10s9-5 9-10V6zM8 12l3 3 5-6',
 'clock':'M12 7v5l4 2M22 12a10 10 0 1 1-20 0 10 10 0 0 1 20 0',
 'map':'m3 5 6-3 6 3 6-3v17l-6 3-6-3-6 3zM9 2v17M15 5v17',
 'search':'M21 21l-6-6M17 9a8 8 0 1 1-16 0 8 8 0 0 1 16 0',
 'copy':'M9 9h12v12H9zM5 15H3V3h12v2',
 'check':'m5 12 4 4L20 5', 'money':'M2 5h20v14H2zM15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0M5 9v6M19 9v6',
 'bolt':'m13 2-9 12h7l-1 8 10-12h-7z', 'lock':'M5 10h14v12H5zM8 10V6a4 4 0 0 1 8 0v4M12 15v3',
 'car':'m3 10 2-6h14l2 6v10h-3v-3H6v3H3zM3 10h18M6 14h2m8 0h2',
 'file':'M5 2h9l5 5v15H5zM14 2v6h5M8 12h8M8 16h8',
}
def icon(name='arrow'):
 return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{PATHS[name]}"/></svg>'
def money(n): return f'{n:,}'.replace(',', '.')
def button(text, href, light=False):
 return f'<a class="button {"cream" if light else ""}" href="{href}">{text}{icon()}</a>'
def badge(text, cls=''): return f'<span class="badge {cls}">{esc(str(text))}</span>'
def intro(kicker, title, body):
 return f'<header class="page-intro wrap"><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="intro-copy">{body}</p></header>'
def note(title, body, kind=''):
 return f'<aside class="note {kind}">{icon("file")}<div><strong>{title}</strong><p>{body}</p></div></aside>'
def sectiontitle(number,title,body=''):
 return f'<div class="section-heading"><div><p class="eyebrow">{number}</p><h2>{title}</h2></div>{f"<p>{body}</p>" if body else ""}</div>'
def card(title, text, glyph='box', num='', extra=''):
 return f'<article class="card reveal"><div class="card-top">{icon(glyph)}<span class="serial">{num}</span></div><h3>{title}</h3><p>{text}</p>{extra}</article>'
def itemlist(items):
 return ', '.join(f'{esc(NAMES.get(i,i))} <b>×{q}</b>' for i,q in items) or 'Sin objeto adicional'
def table(headers, rows, caption=''):
 return '<div class="table-scroll" tabindex="0" role="region" aria-label="'+esc(caption or 'Tabla de consulta')+'"><table>'+ (f'<caption>{caption}</caption>' if caption else '')+'<thead><tr>'+''.join(f'<th scope="col">{h}</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def filters(group, values, search=True, label='Filtrar por clase'):
 return f'<div class="filterbar" data-filter-for="{group}"><div class="filter-chips" role="group" aria-label="{label}">'+''.join(f'<button class="chip {"active" if i==0 else ""}" data-filter="{value}" aria-pressed="{"true" if i==0 else "false"}">{text}</button>' for i,(value,text) in enumerate(values))+f'</div>{f"<label class=\"search\">{icon('search')}<span class=\"sr-only\">Buscar en {group}</span><input type=\"search\" placeholder=\"Buscar…\" data-search=\"{group}\" autocomplete=\"off\"></label>" if search else ""}</div><p class="filter-count" data-count="{group}" aria-live="polite"></p>'
def empty(group): return f'<p class="empty" data-empty="{group}" hidden>No hay resultados con estos filtros. <button data-reset="{group}">Restablecer filtros</button></p>'

NAV=[('index.html','Inicio'),('sistema.html','El sistema'),('normativa.html','Normativa'),('robos.html','Robos'),('implementacion.html','Implementación'),('mafias.html','Mafias / PDM')]
def shell(file,title,body,desc):
 nav=''.join(f'<a href="{f}" {"aria-current=\"page\"" if f==file else ""}>{t}</a>' for f,t in NAV)
 return f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · SIEGA Community</title><meta name="description" content="{esc(desc)}"><meta name="theme-color" content="#111211"><meta property="og:title" content="{title} · SIEGA Community"><meta property="og:description" content="{esc(desc)}"><meta property="og:image" content="https://danigampliss10-sys.github.io/siega-sistema-ilegal/assets/img/hero.png"><link rel="icon" href="assets/img/mark.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/css/site.css"><script defer src="assets/js/site.js"></script></head>
<body><a class="skip" href="#contenido">Saltar al contenido</a><div class="reading-progress" aria-hidden="true"></div>
<header class="site-header"><a class="brand" href="index.html" aria-label="SIEGA Community, inicio"><span class="brand-emblem">{icon('shield')}</span><span class="brand-word">SIEGA<span>Community</span></span></a><button class="menu-toggle" aria-expanded="false" aria-controls="mainnav">Menú<span>☰</span></button><nav id="mainnav" aria-label="Navegación principal">{nav}</nav><a class="header-cta" href="normativa.html">Leer las reglas {icon('arrow')}</a></header>
<main id="contenido">{body}</main>
<footer class="site-footer wrap"><div><a class="footer-brand" href="index.html">SIEGA <span>Community</span></a><p>Sistema ilegal. Historias con consecuencias.</p></div><div><p class="eyebrow">Edición de trabajo · {DATE}</p><p>Reglas acordadas y catálogo de implementación propuesto.<br>Las fichas pendientes no habilitan actividades.</p><a href="content/indice.md">Índice de documentos {icon('arrow')}</a></div></footer>
<button class="back-top" aria-label="Volver arriba">↑</button><div class="toast" role="status" aria-live="polite"></div></body></html>'''

def home():
 body=f'''<section class="hero"><div class="hero-image" role="img" aria-label="Ilustración nocturna de la ciudad, un deportivo naranja y personajes junto al paseo"></div><div class="hero-content wrap"><p class="eyebrow">SIEGA COMMUNITY / SISTEMA ILEGAL</p><h1>La calle tiene<br>sus reglas.<br><span class="brush">Tu historia, también.</span></h1><p>Empieza desde abajo. Encuentra tus contactos.<br>Construye una organización que tenga algo que contar.</p><div class="actions">{button('Descubre el sistema','sistema.html')}{button('Lee la normativa','normativa.html',True)}</div><div class="hero-meta"><span class="status-dot"></span> Del primer encargo a una red organizada.</div></div><div class="hero-bottom"><span>Explora el sistema ↓</span><span>01 / SIEGA STORIES <i></i></span></div></section>
<div class="ribbon"><span>ROL CON SENTIDO</span><b>✳</b><span>PROGRESIÓN CON HISTORIA</span><b>✳</b><span>CADA RECURSO TIENE SU PORQUÉ</span><b>✳</b><span>SIEGA COMMUNITY</span></div>
<section class="wrap section">{sectiontitle('01 / ENCUENTRA TU CAMINO','Todo conectado.<br>Nada <span class="brush">porque sí.</span>','Normas para jugar. Una guía para entenderlo. Un catálogo para construirlo.')}
<div class="feature-grid"><a class="feature-card reveal" href="sistema.html"><span class="feature-art art-one">{icon('people')}</span><div><p class="eyebrow">LA IDEA</p><h3>Empieza pequeño.<br>Hazte un nombre.</h3><p>Civiles, PDB, bandas y mafias. Cada uno tiene su papel y sus límites.</p><span class="button cream">Entiende el sistema {icon()}</span></div></a><a class="feature-card reveal" href="normativa.html"><span class="feature-art art-two">{icon('book')}</span><div><p class="eyebrow">LA NORMATIVA</p><h3>Buen rol.<br>Reglas claras.</h3><p>Reglas numeradas, índice por capítulos y condiciones de cada actividad.</p><span class="button cream">Abre el manual {icon()}</span></div></a><a class="feature-card reveal" href="implementacion.html"><span class="feature-art art-three">{icon('tool')}</span><div><p class="eyebrow">LA IMPLEMENTACIÓN</p><h3>Del botín<br>al siguiente paso.</h3><p>Materiales, probabilidades, recetas, mesas y contactos con una función concreta.</p><span class="button cream">Consulta el catálogo {icon()}</span></div></a></div></section>
<section class="section contrast"><div class="wrap">{sectiontitle('02 / EL RECORRIDO','Una actividad.<br><span class="brush">Muchas conexiones.</span>')}
<div class="route-diagram"><article><span>01</span>{icon('box')}<h3>Consigue</h3><p>Botín y materiales según la procedencia del robo.</p></article><b aria-hidden="true">→</b><article><span>02</span>{icon('tool')}<h3>Prepara</h3><p>Transforma materiales en herramientas útiles.</p></article><b aria-hidden="true">→</b><article><span>03</span>{icon('people')}<h3>Conecta</h3><p>Acuerdos, encargos y suministros a través del rol.</p></article><b aria-hidden="true">→</b><article><span>04</span>{icon('arrow')}<h3>Progresa</h3><p>Tu trayectoria abre oportunidades; no basta con acumular dinero.</p></article></div>
<div class="metrics"><div><strong>7</strong><span>Clases · E a S+</span></div><div><strong>12</strong><span>Mesas planificadas</span></div><div><strong>{len(RECIPES)}</strong><span>Fichas de recetas</span></div><div><strong>20</strong><span>Contactos propuestos</span></div></div><p class="small">El catálogo es una base de diseño. Incluye reservas y decisiones pendientes, identificadas en cada ficha.</p></div></section>
<section class="wrap section">{sectiontitle('03 / CONSULTA A TU RITMO','Cada cosa en <span class="brush">su sitio.</span>')}<div class="link-list">'''
 for n,(file,title,desc) in enumerate([('robos.html','Tabla de robos','Clases, aforos, policías, rehenes y salida.'),('implementacion.html#botin','Botín y economía','Recompensas del grupo, materiales y probabilidades.'),('implementacion.html#mesas','Mesas y recetas','Especialización, ingredientes y resultados.'),('mafias.html','PDM y mafias','Suministro, encargos y progresión de las organizaciones.')],1):
  body+=f'<a href="{file}"><span class="serial">0{n}</span><div><h3>{title}</h3><p>{desc}</p></div>{icon()}</a>'
 body+='</div></section>'
 return body

def system():
 body=intro('01 / GUÍA DEL SISTEMA','De la calle<br>a tu <span class="brush">propia historia.</span>','Una economía ilegal que empieza con actividades pequeñas y crece con preparación, relaciones y constancia. El nivel organiza el acceso; el rol da sentido al camino.')
 body+='<section class="wrap section tight"><div class="split-story"><div><h2>El primer día<br>no es el último nivel.</h2><p>Un civil puede buscar actividades E y D, conseguir equipo básico y tratar con otros personajes. Una PDB comienza con una identidad común y tiene acceso hasta C. Ambos deben descubrir sus oportunidades dentro del rol.</p><p>Comprar un cuchillo resuelve una necesidad inmediata. Fabricarlo exige reunir materiales y encontrar la mesa adecuada. Conseguir un plano de arma de fuego representa otra clase de relación y preparación.</p></div><aside class="quote-card"><span class="eyebrow">EL PRINCIPIO</span><blockquote>El progreso se juega.<br><span class="brush">No se regala.</span></blockquote><p>Sin ascensos automáticos por puntos, sin un plazo público que garantice subir y sin acceso libre a todo desde el inicio.</p></aside></div></section>'
 body+='<section class="wrap section">'+sectiontitle('02 / ORGANIZACIONES','Un lugar para <span class="brush">cada grupo.</span>')+'<div class="level-ladder">'
 for mark,name,text,access in [('00','Civil ilegal','Actividades propias o pequeños grupos, respetando el aforo de cada robo.','E · D'),('01','Proyecto de Banda','Entre 3 y 6 integrantes. Construye identidad, contactos y una trayectoria común.','E · D · C'),('02','Banda N1','Entre 5 y 10 integrantes. Primer escalón de banda oficial, con hasta 3 camellos.','Hasta B'),('03','Banda N2','Organización consolidada, con hasta 6 camellos. Plantilla máxima pendiente de cierre.','Hasta A'),('04','Banda N3','Hasta 9 camellos. Acceso a los golpes superiores cuando estén definidos.','Hasta S+')]:
  body+=f'<article><span class="level-number">{mark}</span><div><h3>{name}</h3><p>{text}</p></div>{badge(access)}</article>'
 body+='</div>'+note('Los camellos reciben encargos','No son refuerzos de los robos de la banda. Mantienen el acceso de civil a E y D, trabajan para una banda dentro del rol y no llevan un subrol de Discord.')+'</section>'
 body+='<section class="section contrast"><div class="wrap">'+sectiontitle('03 / SUMINISTRO Y RELACIONES','La red se construye <span class="brush">jugando.</span>')+'<div class="supply-flow">'
 for name,desc in [('Coordinación','Supervisa el conjunto del sistema.'),('PDM / mafias','Consiguen suministro, generan encargos y desarrollan contactos.'),('Bandas','Preparan actividades y pueden encargar trabajo a otros grupos.'),('PDB','Se buscan la vida y crean relaciones para avanzar.')]:
  body+=f'<article>{icon("people")}<h3>{name}</h3><p>{desc}</p></article>'
 body+='</div><p>Al abrir el servidor puede haber PDM y PDB sin bandas oficiales todavía. En esa etapa, la mafia puede contactar directamente con una PDB que haya generado una trayectoria. El reparto de relaciones evoluciona IC; no es una asignación pública permanente.</p>'+button('Leer el manual de PDM','mafias.html')+'</div></section>'
 body+='<section class="wrap section">'+sectiontitle('04 / HERRAMIENTAS, PLANOS Y MATERIALES','Prepararse también <span class="brush">es rol.</span>')+'<div class="card-grid">'
 body+=card('Contactos de calle','Cada vendedor tiene su producto y su diálogo: una ganzúa, una avanzada, un spray o un arma blanca. Las compras usan dinero negro.','people','01')
 body+=card('Mesas físicas','Cada mesa tiene una especialidad. Se muestran ingredientes, cantidades y resultado. El NPC conversa; la mesa fabrica.','tool','02')
 body+=card('Planos específicos','Las armas de fuego requieren un plano. Una PDB puede recibir uno en una misión de mafia, pero eso no le permite hacer robos de clase B.','file','03')
 body+=card('Materiales con origen','La chatarra de pequeñas actividades alimenta el trabajo básico. Los componentes técnicos aparecen en suministros y actividades de mayor preparación.','box','04')
 body+=card('Cuentas del grupo','Los botines se calculan para el grupo completo, no por participante. Repartirlos es una decisión de rol.','money','05')
 body+=card('Información que se descubre','La guía no entrega ubicaciones. Los contactos, relaciones y oportunidades se encuentran dentro del juego.','map','06')
 body+='</div></section><section class="wrap section tight">'+note('Qué sigue pendiente','Casas y sus tipos, cultivo y laboratorios, ubicaciones, varios golpes superiores y decisiones concretas del suministro siguen reservados. No se presentan como sistemas ya disponibles.')+button('Ver reglas y límites','robos.html')+'</section>'
 return body

def rules_page():
 body=intro('02 / NORMATIVA DE LA FACCIÓN ILEGAL','Buen rol.<br>Reglas <span class="brush">claras.</span>',INTRO)
 body+='<div class="wrap doc-actions">'+badge('Edición de revisión')+'<a class="text-link" href="content/normativa.md" download>Descargar Markdown '+icon('file')+'</a><button class="text-link" data-print>Imprimir / guardar PDF '+icon('book')+'</button></div><div class="wrap doc-layout"><aside class="toc"><p class="eyebrow">ÍNDICE</p><nav aria-label="Capítulos de la normativa">'
 for i,(title,_) in enumerate(RULES,1): body+=f'<a href="#capitulo-{i}"><span>{i:02}</span>{title}</a>'
 body+='</nav><a class="toc-table" href="robos.html">Tabla de robos '+icon('arrow')+'</a></aside><div class="rules-body">'
 for i,(title,parts) in enumerate(RULES,1):
  body+=f'<section class="rule-chapter" id="capitulo-{i}"><div class="chapter-title"><span>{i:02}</span><h2>{title}</h2></div>'
  for j,(sub,text) in enumerate(parts,1): body+=f'<article id="regla-{i}-{j}" class="rule"><h3><a href="#regla-{i}-{j}" aria-label="Enlace a la regla {i}.{j}">{i}.{j}</a> {sub}</h3><p>{text}</p></article>'
  body+='</section>'
 body+='</div></div>'
 return body

REGISTER='Fecha (DD/MM):\nHora aproximada de inicio:\nHora aproximada de fin:\nTipo de robo y clase:\nPersonas involucradas:\nBotín / recompensa:\nResultado: con éxito / sin éxito'
def robberies():
 body=intro('03 / MANUAL DE ROBOS','Conoce el límite.<br>Juega la <span class="brush">escena.</span>','Cada actividad tiene su ficha. El mínimo policial habilita el robo; el aforo total incluye a quien conduce, vigila o apoya fuera.')
 body+='<section class="wrap section tight"><div class="rules-strip"><div>'+icon('lock')+'<strong>/robos desde C</strong><p>Aceptación antes de acudir a ejecutarlo.</p></div><div>'+icon('shield')+'<strong>Fuego desde B</strong><p>En E, D y C: solo armas blancas.</p></div><div>'+icon('car')+'<strong>Apoyo desde C</strong><p>Bloqueos y superdeportivos desde C.</p></div></div>'
 body+=table(['Clase','Acceso','Cupo común','Armamento / escena'],[['E','Civil y organizaciones','Sin cupo normativo','Armas blancas · actividad pequeña'],['D','Civil y organizaciones','Sin cupo normativo','Armas blancas · sin bloqueos ni tiroteos'],['C','PDB y bandas','3 al día por organización','Blancas · bloqueos y apoyo dentro del aforo'],['B','Banda N1 o superior','3 a la semana','Armas de fuego y tiroteos permitidos según rol'],['A','Banda N2 o superior','1 a la semana','Preparación y coordinación elevada'],['S','Banda N3','1 cada dos semanas','Según ficha; tren definido parcialmente'],['S+','Banda N3','1 al mes','Golpes futuros, sin ficha habilitada']],'Clases y cupos')
 body+=note('El cupo se gasta al ejecutar','La aceptación no consume un intento. Empezar el robo sí, salga bien o mal. Los cupos son comunes por clase y no se reinician cambiando de participantes.')+'</section>'
 body+='<section class="wrap section">'+sectiontitle('01 / FICHAS POR ACTIVIDAD','Elige tu <span class="brush">clase.</span>','Abre una ficha para consultar condiciones, avisos y salida.')+filters('robos',[('all','Todas')]+[(c,c) for c in ['E','D','C','B','A','S']])+'<div class="robbery-list">'
 for r in ROB:
  id,name,cls,cops,inside,total,host,exit,notice,req,cash,guarantee,roll,state=r
  body+=f'<details class="robbery" data-group="robos" data-category="{cls}" data-text="{esc(name+" "+cls)}" id="robo-{id}"><summary><span class="class-mark">{cls}</span><div><h3>{name}</h3><span>{"Ficha parcial" if id=="blindado" else "Condiciones de rol"}</span></div><span class="summary-metric"><b>{cops}</b> policía{("s" if cops!=1 else "")}</span><span class="summary-metric"><b>{total}</b> total</span><span class="expand">+</span></summary><div class="robbery-content"><dl class="facts"><div><dt>Robando / en el asalto</dt><dd>{inside}</dd></div><div><dt>Máximo total</dt><dd>{total}</dd></div><div><dt>Rehenes máximos</dt><dd>{host}</dd></div></dl><div class="two-columns"><div><h4>Avisos y autorización</h4><p>{notice}</p></div><div><h4>Salida y espera</h4><p>{exit}</p></div></div><p class="small">{state}</p><a class="text-link" href="implementacion.html#botin-{id}">Ver propuesta de botín {icon()}</a></div></details>'
 body+='</div>'+empty('robos')+'</section>'
 body+='<section class="section contrast"><div class="wrap">'+sectiontitle('02 / DESPUÉS DEL ROL','Registra el resultado.<br><span class="brush">También si fallas.</span>')+'<div class="split-story"><div><p>Desde clase C, cualquiera de los participantes debe registrar el robo. Hazlo al acabar, cuando estés en una zona tranquila. El plazo máximo es de <strong>12 horas</strong>.</p><p>Fecha, horas aproximadas, participantes, botín y resultado. Un solo registro por robo. Guarda la grabación durante al menos <strong>48 horas</strong>.</p>'+note('Reinicio de cupos','Cada día a las 00:00; semanales, del domingo al lunes; mensuales, el día 1. Hora peninsular. El anclaje del calendario quincenal S queda pendiente.')+'</div><div class="template-card"><div class="card-top"><h3>Plantilla de registro</h3><button class="icon-button" data-copy="registro" aria-label="Copiar plantilla">'+icon('copy')+'</button></div><pre id="registro">'+REGISTER+'</pre><button class="button cream" data-copy="registro">Copiar plantilla '+icon('copy')+'</button></div></div></div></section>'
 body+='<section class="wrap section">'+sectiontitle('03 / MÁS ADELANTE','Reservado para <span class="brush">otra historia.</span>')+table(['Actividad','Clase','Estado'],[['Casas','D','Aparcado. Primer tipo con 1 policía; resto de requisitos pendientes.'],['Furgón blindado','A','Marco y recompensa propuestos; operativa final pendiente.'],['Union Depository','Por definir','Fuera de la lista habilitada.'],['Yate','Por definir','Pendiente.'],['Humane Labs','S','Pendiente.'],['Diamond Casino','S+','Pendiente.'],['Banco Central','S+','Pendiente.'],['Contenedores industriales','Por definir','Pequeño y grande pendientes.']],'Actividades pendientes')+'<p class="small">Farmacias y avión de carga no forman parte del catálogo actual.</p></section>'
 return body


def implementation():
 b=intro('CATÁLOGO / IMPLEMENTACIÓN','Cada pieza tiene <span class="brush">su propósito.</span>','Propuesta de configuración para el equipo. Cantidades por robo completo y grupo, salvo unidades indicadas. Todo pago monetario utiliza black_money. Ubicaciones a cargo de la dirección.')
 b+='<nav class="wrap subnav">'+''.join(f'<a class="button cream" href="#{s}">{n}</a>' for s,n in [('botin','Botín'),('materiales','Materiales'),('mesas','12 mesas'),('recetas','Recetas'),('npcs','20 contactos')])+'</nav>'
 b+='<section class="wrap section" id="botin">'+sectiontitle('01 / RECOMPENSAS','Botín por actividad','Una tirada de la tabla por robo: los porcentajes son alternativas, no premios acumulados. Dividir el presupuesto entre puntos; no multiplicarlo.')
 for r in ROB:
  b+=f'<details class="robbery" id="botin-{r[0]}"><summary>{badge(r[2])}<h3>{r[1]}</h3><span class="expand">+</span></summary><div class="robbery-content"><h4>Requisito</h4><p>{r[9]}</p><h4>Dinero negro</h4><p>{money(r[10][0])+"–"+money(r[10][1]) if r[10] else "Sin cantidad monetaria definida"}</p><h4>Objetos garantizados</h4><p>{itemlist(r[11])}</p>'+table(['Probabilidad','Resultado'],[[str(p)+'%',itemlist(items)] for p,items in r[12]])+f'<p class="small">{r[13]}</p></div></details>'
 b+=note('24/7 y LTD: caja fuerte opcional','Añade 500–800 de dinero negro al presupuesto de registradoras. Total máximo combinado: 1.700. Una tirada extra: 40% circuito ×1; 30% mecanismo ×1; 20% chatarra ×3; 10% sin extra.')+'</section>'
 b+='<section class="wrap section" id="materiales">'+sectiontitle('02 / CATÁLOGO','Materiales y procedencia')+table(['Material / identificador','Familia','Procedencia','Utilidad'],[[m[1]+'<br><code>'+m[0]+'</code>',m[2],m[3],m[4]] for m in MATERIALS])+'</section>'
 b+='<section class="wrap section" id="mesas">'+sectiontitle('03 / TALLERES','12 mesas especializadas','Propuesta: 11 mesas iniciales y una reservada. Las recetas pendientes no se habilitan hasta cerrar sus materiales.')+'<div class="card-grid">'
 for t in TABLES:
  b+=card(t[0]+' · '+t[1],t[2]+'<br>'+t[4]+'<br><strong>'+t[3]+'</strong>','tool',extra=f'<p>{sum(r["table"]==t[0] for r in RECIPES)} recetas del catálogo</p>')
 b+='</div></section><section class="wrap section" id="recetas">'+sectiontitle('04 / FABRICACIÓN','Ingredientes claros','Cantidades por fabricación. Los planos de armas de fuego se obtienen por rol; aprender un plano no entrega materiales ni autoriza a saltarse las clases.')
 b+=table(['Mesa','Resultado','Ingredientes','Plano','Observaciones'],[[r['table'],r['name']+' ×'+str(r['quantity']),itemlist(r['parts'].items()) if r['parts'] else 'Pendiente', 'Sí' if r['plan'] else 'No',r['note']] for r in RECIPES])+note('Aprendizaje de planos','Queda por decidir si se vincula al personaje o a la mesa. La fabricación siempre requiere el plano aplicable y todos los ingredientes.')+'</section>'
 b+='<section class="wrap section" id="npcs">'+sectiontitle('05 / CONTACTOS','20 contactos con oficio','15 vendedores de armas blancas y 5 contactos especializados. Interacción mediante diálogo; las mesas conservan su interfaz de fabricación. Sin ubicaciones públicas.')+table(['Contacto','Venta / intercambio','Precio en black_money'],[[str(i+1)+' · '+n,n,money(p)] for i,(n,p) in enumerate(NPC_WEAPONS)]+[['16 · Ganzúas','Ganzúa normal','1.200'],['17 · Cerraduras','Ganzúa avanzada','4.500'],['18 · Herramientas','Hacha / pala / Torx / kit / USB','2.500 / 2.000 / 2.000 / 3.500 / 1.000'],['19 · Pintura','Spray','Por definir'],['20 · Recuperador','1 rueda por 5 metalscrap','Trueque']])+note('Diálogos conectados','El vendedor de ganzúas puede recomendar al especialista en cerraduras avanzadas mediante pistas IC. Favores y venta de droga se definen aparte; aquí no se inventan sus recompensas.')+'</section>'
 return b

def mafias():
 return intro('GUÍA DE ORGANIZACIÓN','Construir una <span class="brush">red.</span>','Manual de coordinación para PDM y mafias. Las relaciones, los encargos y la confianza se desarrollan dentro del rol.')+'<section class="wrap section"><div class="card-grid">'+''.join(card(t,p,'people') for t,p in [
 ('Inicio como PDM','Se plantea una apertura con al menos dos proyectos de mafia. La postulación no entrega un arsenal ilimitado: capital, existencias y medios iniciales deben concretarse.'),
 ('Cadena de suministro','Coordinación → mafias → bandas → PDB. Al comienzo, cuando aún no existan bandas, las mafias pueden contactar directamente con PDB que hayan desarrollado una trayectoria.'),
 ('Trabajo propio','Buscar suministros, organizar transportes, gestionar existencias, preparar encargos y cerrar acuerdos. La mafia debe generar historias y tener actividad propia.'),
 ('Encargos con continuidad','Proponer una tarea, negociar condiciones, comprobar la entrega y resolver la recompensa. El fracaso puede afectar a la confianza; no implica una sanción OOC automática.'),
 ('Planos y armamento','Los planos pueden ser recompensa de una misión. Conseguir un plano no regala un arma ni sus materiales. Una PDB no se convierte en una categoría nueva por obtenerlo.'),
 ('Ascensos por trayectoria','Las mafias valoran constancia, eficacia y fiabilidad con supervisión de coordinación. No hay ascenso automático por puntos, número de robos o días transcurridos.'),
 ('Drogas y distribución','En el planteamiento inicial, las mafias producen y distribuyen encargos de venta. Comisiones y condiciones se negocian IC. Los laboratorios de bandas quedan para una fase posterior.'),
 ('Límites del papel','La mafia se centra en distribución, contactos y encargos; no actúa como refuerzo en los robos de las bandas. La organización de PDB y bandas se resuelve mediante rol.')])+'</div>'+note('Pendientes de coordinación','Capital y stock inicial de cada PDM, catálogo final de suministros, proceso productivo de drogas y evaluación interna. No se presentan como reglas aprobadas.')+'</section>'

if __name__=='__main__':
 validate()
 (ROOT/'content').mkdir(exist_ok=True)
 pages=[('index.html','Inicio',home()),('sistema.html','El sistema',system()),('normativa.html','Normativa',rules_page()),('robos.html','Robos',robberies()),('implementacion.html','Implementación',implementation()),('mafias.html','Mafias y PDM',mafias())]
 for file,title,body in pages: (ROOT/file).write_text(shell(file,title,body,'Sistema ilegal de SIEGA Community: '+title),encoding='utf-8')
 md='# Normativa ilegal · SIEGA Community\n\n'+INTRO+'\n\n'
 for i,(title,items) in enumerate(RULES,1):
  md+=f'## {i}. {title}\n\n'
  for j,(name,text) in enumerate(items,1): md+=f'### {i}.{j} {name}\n\n{text}\n\n'
 (ROOT/'content/normativa.md').write_text(md,encoding='utf-8')
 (ROOT/'content/indice.md').write_text('# SIEGA Community\n\n'+ '\n'.join(f'- [{t}](../{f})' for f,t in NAV),encoding='utf-8')
 (ROOT/'content/catalogo.json').write_text(json.dumps(dict(materiales=MATERIALS,robos=ROB,mesas=TABLES,recetas=RECIPES,npcs=NPC_WEAPONS),ensure_ascii=False,indent=2),encoding='utf-8')
 print('Generadas 6 páginas; catálogo validado.')
