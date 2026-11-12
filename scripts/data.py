"""Catálogo de diseño de juego. No es una configuración activa de FiveM."""
MATERIALS = [
 ('il_madera','Tablones de madera','Común','Palés','Mangos y bate de madera',70),
 ('metalscrap','Chatarra de metal','Común','Parquímetros, ruedas, tiendas y desguace','Procesado de acero, herramientas y piezas',60),
 ('iron','Hierro','Común','Desguace','Cabezas de herramientas y hojas sencillas',180),
 ('metal','Metal','Común','Desguace','Herramientas y refuerzos',120),
 ('steel','Acero','Procesado','Procesado de chatarra y desguace','Herramientas resistentes y fabricación avanzada',300),
 ('plastic','Plástico','Común','Parquímetros, tiendas y desguace','Carcasas y herramientas',35),
 ('copper','Cobre','Común','Desguace y tren','Electrónica y munición',75),
 ('rubber','Caucho','Común','Ruedas y desguace','Agarres y útiles',40),
 ('glass','Vidrio','Común','Tumbas y licorerías','Reserva de catálogo; sin receta aprobada',50),
 ('aluminum','Aluminio','Común','Desguace y tren','Placas y fabricación avanzada',100),
 ('il_mango','Mango','Procesado','Mesa de madera','Agarre de cuchillos, hachas y herramientas',180),
 ('il_pieza_coche','Pieza de coche','Oficio','Ruedas y desguace','Dispositivo de pinchos',None),
 ('il_mecanismo','Mecanismo','Oficio','Cajas fuertes, desguace, bancos y tren','Ganzúa avanzada y electrónica',250),
 ('il_alambre','Alambre rígido','Oficio','Fuente pendiente','Ganzúa avanzada; cerrar suministro antes de habilitar',80),
 ('il_cinta','Cinta aislante','Oficio','Registradoras 24/7 y LTD','Agarres, placas y ganzúa avanzada',50),
 ('il_circuito','Placa electrónica','Técnico','Cajeros, cajas fuertes y robos mayores','Dispositivos y fabricación',350),
 ('il_aleacion','Aleación','Técnico','Tren','Fabricación especializada',500),
 ('il_piezas_cortas','Piezas de arma corta','Técnico','Fleeca, Ammu-Nation y bancos A','Recetas de pistolas con plano',None),
 ('il_piezas_compactas','Piezas de arma compacta','Técnico','Fuente pendiente','Micro SMG: receta reservada',None),
 ('il_lote_municion','Lote de munición','Técnico','Fleeca y Ammu-Nation','Lote de 12 unidades de 9 mm',None),
 ('il_mercancia','Mercancía variada','Botín','Tiendas','Mercancía de rol; salida comercial por definir',None),
 ('il_prendas','Prendas','Botín','Tiendas de ropa','Mercancía textil',None),
 ('il_tinta','Tinta','Botín','Tiendas de tatuajes','Suministro de oficio',None),
 ('il_alcohol','Alcohol','Botín','Licorerías','Mercancía propia del comercio',None),
 ('inherited_watch','Reloj heredado','Valioso','Tumbas y pawnshop','Objeto de valor; no es un ingrediente',None),
 ('rolex','Reloj','Valioso','Tumbas y pawnshop','Objeto de valor',None),
 ('goldchain','Cadena de oro','Valioso','Tumbas, pawnshop y joyería','Objeto de valor',None),
 ('gold_ring','Anillo de oro','Valioso','Tumbas, pawnshop y joyería','Objeto de valor',None),
 ('diamond_ring','Anillo de diamantes','Valioso','Pawnshop y joyería','Objeto de valor',None),
 ('diamond','Diamante','Valioso','Tumbas, pawnshop y joyería','Gema; hallazgo excepcional en tumbas',None),
 ('ruby','Rubí','Valioso','Pawnshop y joyería','Gema',None),
 ('emerald','Esmeralda','Valioso','Pawnshop y joyería','Gema',None),
 ('jewelry','Joyas','Valioso','Joyería','Botín del establecimiento',None),
]

# id, nombre, clase, policías, dentro, total, rehenes, salida, aviso, requisito, dinero, garantizado, sorteo, estado
ROB = [
 ('favores','Favores de NPC','E',0,'1','1','0','Al completar el encargo','/entorno opcional','Según el favor',None,[],[],'Encargos y recompensas a definir'),
 ('drogas','Venta de droga','E',1,'—','2','0','Sin espera policial','Automático al intentar vender + /entorno al comenzar, con personas y vehículo','Mercancía para la venta',None,[],[],'Precio y cantidades a cargo de dirección'),
 ('madera','Palés de madera','E',1,'—','2','0','Sin espera policial','Automático + /entorno al comenzar','Hacha de trabajo',None,[('il_madera',3)],[(25,[('metalscrap',1)]),(75,[])],'Dinero no previsto; materiales'),
 ('ruedas','Robo de ruedas','E',1,'—','2','0','Sin espera policial','/entorno antes de la primera rueda; sin aviso automático','Llave Torx',None,[],[(70,[('rueda',1)]),(25,[('rubber',2),('steel',1)]),(5,[('il_pieza_coche',1)])],'Una tirada por rueda; canje de rueda por 5 de chatarra'),
 ('parquimetros','Parquímetros','D',1,'—','2','0','Al terminar','Automático; /entorno manual no obligatorio','Arma blanca válida para golpear el parquímetro',(400,700),[('metalscrap',2),('plastic',1)],[],'Botín por parquímetro'),
 ('cajeros','Cajeros ATM','D',1,'—','2','0','Al terminar','Automático; /entorno manual no obligatorio','Herramienta pendiente de concretar',(1500,2500),[],[(20,[('il_circuito',1)]),(80,[])],'Herramienta pendiente'),
 ('tumbas','Tumbas','D',1,'—','2','0','Al terminar','Automático; /entorno manual no obligatorio','Pala',(500,900),[],[(35,[('rolex',1)]),(25,[('goldchain',1)]),(20,[('metalscrap',2),('glass',1)]),(15,[('inherited_watch',1)]),(4,[('gold_ring',1)]),(1,[('diamond',1)])],'Una tirada por tumba'),
 ('247','24/7 y LTD','D',2,'1–2','2','2, incluido el tendero si se utiliza','5 min desde terminar; si llega policía, negociar','Automático + /entorno con personas y vehículo','Arma blanca para registradora; ganzúa para caja fuerte opcional',(800,900),[('il_mercancia',1)],[(40,[('il_cinta',1)]),(30,[('plastic',2)]),(20,[('metalscrap',1)]),(10,[])],'Caja fuerte: +500–800; máximo conjunto 1.700'),
 ('licoreria','Licorerías','D',2,'1–2','2','2, incluido el tendero si se utiliza','5 min desde terminar; si llega policía, negociar','Automático + /entorno con personas y vehículo','Arma blanca',(600,800),[],[(60,[('il_alcohol',2)]),(25,[('il_alcohol',3)]),(15,[('il_alcohol',1)])],'Además, 20% independiente de vidrio ×1'),
 ('peluqueria','Peluquerías','D',2,'1–2','2','2, incluido el tendero si se utiliza','5 min desde terminar; si llega policía, negociar','Automático + /entorno con personas y vehículo','Arma blanca',(600,800),[],[(30,[('il_mercancia',1)]),(70,[])],'Base de equilibrio'),
 ('tatuajes','Tiendas de tatuajes','D',2,'1–2','2','2, incluido el tendero si se utiliza','5 min desde terminar; si llega policía, negociar','Automático + /entorno con personas y vehículo','Arma blanca',(600,800),[],[(50,[('il_tinta',1)]),(30,[('il_tinta',2)]),(20,[])],'Base de equilibrio'),
 ('libreria','Librerías','D',2,'1–2','2','2, incluido el tendero si se utiliza','5 min desde terminar; si llega policía, negociar','Automático + /entorno con personas y vehículo','Arma blanca',(600,800),[],[(60,[('il_mercancia',1)]),(25,[('il_mercancia',2)]),(15,[])],'Base de equilibrio'),
 ('ropa','Tiendas de ropa','D',2,'1–2','2','2, incluido el tendero si se utiliza','5 min desde terminar; si llega policía, negociar','Automático + /entorno con personas y vehículo','Arma blanca',(600,800),[],[(60,[('il_prendas',1)]),(30,[('il_prendas',2)]),(10,[])],'Base de equilibrio'),
 ('importacion','Importación','D',1,'—','3','0','Huida y entrega; no esperar a policía','Automático al salir con el coche; sin /entorno obligatorio','Contrato de importación',None,[],[],'Localizador de 5 min; recompensa pendiente'),
 ('desguace','Desguace','C',2,'1–2','3','2','Esperar a policía; negociar si hay rehenes','Aceptación por /robos + /entorno','Palanca de trabajo',(12000,18000),[],[(30,[('metalscrap',6),('steel',2)]),(20,[('copper',3),('plastic',2)]),(20,[('rubber',3),('il_pieza_coche',1)]),(15,[('steel',3),('aluminum',2)]),(10,[('iron',4),('metal',2)]),(5,[('il_mecanismo',1),('il_circuito',1)])],'Robo de objetos del recinto; no desguace de vehículos'),
 ('pawnshop','Pawnshop','C',3,'1–3','4','2','Esperar a policía; negociar si hay rehenes','Aceptación por /robos + /entorno','Ganzúa avanzada',(14000,20000),[],[(25,[('goldchain',2)]),(20,[('rolex',2)]),(15,[('gold_ring',1)]),(10,[('inherited_watch',1)]),(10,[('diamond_ring',1)]),(5,[('diamond',1)]),(5,[('ruby',1)]),(5,[('emerald',1)]),(5,[])],'Apoyo exterior incluido en el total'),
 ('fleeca','Fleeca','B',4,'2–3','5','4; recepcionista opcional incluido','Esperar dentro a policía','Aceptación por /robos + /entorno','USB troyano por intento; taladro sujeto a ficha final',(32000,45000),[],[(35,[('il_circuito',2)]),(30,[('il_lote_municion',1)]),(25,[('il_piezas_cortas',1)]),(10,[('il_mecanismo',2)])],'Negociación con los rehenes disponibles'),
 ('joyeria','Joyería','B',5,'2–4','6','4 reales; sin dependiente imaginario','Esperar dentro; negociar si hay rehenes','Aceptación por /robos + /entorno','Herramienta de corte: objeto pendiente',(28000,42000),[],[(30,[('jewelry',2)]),(20,[('goldchain',2)]),(20,[('diamond_ring',1)]),(10,[('gold_ring',1)]),(8,[('emerald',1)]),(6,[('ruby',1)]),(4,[('diamond',1)]),(2,[])],'Catálogo de joyas diversificado'),
 ('ammunation','Ammu-Nation','B',5,'2–4','6','4 reales; sin dependiente imaginario','Esperar dentro; negociar si hay rehenes','Aceptación por /robos + /entorno','Ganzúa avanzada; kit solo si se confirma en ficha',(25000,38000),[],[(35,[('il_lote_municion',2)]),(25,[('steel',2),('copper',1)]),(25,[('il_piezas_cortas',1)]),(15,[])],'No entrega armas terminadas'),
 ('paleto','Banco Paleto','A',6,'2–4','8','6','Esperar a policía y desarrollar la intervención','Aceptación por /robos + /entorno','Dispositivos de acceso por concretar',(60000,75000),[],[(45,[('il_circuito',2)]),(25,[('il_piezas_cortas',1)]),(20,[('il_mecanismo',2)]),(10,[])],'Mínimo de 60.000 confirmado'),
 ('sandy','Banco de Sandy','A',6,'2–4','8','6','Esperar a policía y desarrollar la intervención','Aceptación por /robos + /entorno','Dispositivos de acceso por concretar',(60000,75000),[],[(45,[('il_circuito',2)]),(25,[('il_piezas_cortas',1)]),(20,[('il_mecanismo',2)]),(10,[])],'Mismo marco que Paleto; botín equivalente propuesto'),
 ('blindado','Furgón blindado','A',6,'Hasta 4 en el asalto','6','0','Enfrentamiento armado; cierre operativo pendiente','Solicitud y avisos: protocolo final pendiente','Equipo de interceptación pendiente',(60000,70000),[('metalscrap',4),('steel',2)],[(40,[('il_mecanismo',1)]),(30,[('il_circuito',1)]),(20,[('copper',3)]),(10,[])],'Sin negociación; mínimo de asaltantes pendiente'),
 ('tren','Tren de mercancías','S',8,'3–6','6','0','Pueden huir al terminar o abandonar antes','Aceptación por /robos + /entorno + automático al comenzar','Equipo de acceso pendiente',(80000,95000),[('steel',8),('aluminum',6),('copper',6)],[(40,[('il_circuito',2)]),(30,[('il_mecanismo',2)]),(20,[('il_aleacion',1)]),(10,[])],'Sin negociación; materiales para fabricación, no reventa extra'),
]

TABLES = [
 ('T01','Carpintería','Mangos de madera','base','Transformar tablones en un agarre útil; la madera no se convierte en metal.'),
 ('T02','Preparación de metales','Acero de trabajo','base','Dar una salida concreta a la chatarra obtenida en actividades pequeñas.'),
 ('T03','Cerrajería','Ganzúas y acceso','base','Separar las herramientas de acceso de las armas y la electrónica.'),
 ('T04','Útiles de trabajo','Recogida y mantenimiento','base','Fabricar el equipo básico para conseguir materiales.'),
 ('T05','Armas blancas · filo','Cuchillos y machete','base','Hojas, mecanismos y mangos acordes a cada objeto.'),
 ('T06','Armas blancas · impacto','Bate, martillo y útiles','base','El bate de madera usa madera y cinta; no necesita hierro.'),
 ('T07','Hachas','Herramientas de corte pesado','base','Diferenciar el hacha de trabajo del arma; receta de piedra en revisión.'),
 ('T08','Electrónica','Dispositivos y reparación','base','Circuitos y cobre tienen un destino concreto. El equipo de casas queda aparcado.'),
 ('T09','Logística','Spray, pinchos y placas','base','Preparación para actividades permitidas; fabricar no amplía permisos de uso.'),
 ('T10','Armas cortas','SNS y pistola','controlada','Requiere plano específico y componentes. Sin armas policiales.'),
 ('T11','Armas compactas','Micro SMG','reservada','Mesa futura. No se habilita hasta cerrar el origen de sus piezas.'),
 ('T12','Munición','Lotes de 9 mm','controlada','Fabricación en cantidades pequeñas con plano y lote de munición.'),
]
RECIPES=[]
def recipe(name,table,parts,plan=False,quantity=1,note='Propuesta',output=None):
 RECIPES.append(dict(name=name,table=table,parts=parts,plan=plan,quantity=quantity,note=note,output=output))
recipe('Mango','T01',{'il_madera':2,'rubber':1},output='il_mango')
recipe('Acero de trabajo','T02',{'metalscrap':5},output='steel')
recipe('Ganzúa','T03',{'metalscrap':3,'steel':1},output='lockpick')
recipe('Ganzúa avanzada','T03',{'steel':2,'metal':2,'il_alambre':1,'il_mecanismo':1,'il_cinta':1},True,note='Pendiente de suministro de alambre',output='advancedlockpick')
recipe('Llave Torx','T03',{'metalscrap':2,'steel':2,'il_mecanismo':1})
recipe('Destornillador','T03',{'steel':2,'plastic':1})
recipe('Palanca de trabajo','T03',{'steel':3,'metalscrap':2,'rubber':1},True,note='Objeto de trabajo distinto del arma palanca',output='il_palanca')
recipe('Cizalla','T03',{'steel':4,'il_mecanismo':1,'rubber':1},True)
recipe('Hacha de trabajo','T04',{'iron':2,'metal':1,'il_mango':1,'rubber':1})
recipe('Pala','T04',{'steel':2,'il_madera':1})
recipe('Kit de herramientas','T04',{'metalscrap':6,'steel':3,'rubber':2})
recipe('Cuchillo','T05',{'iron':2,'il_mango':1})
recipe('Navaja automática','T05',{'metalscrap':4,'steel':3,'il_mecanismo':1},True)
recipe('Daga','T05',{'steel':3,'metal':1,'il_mango':1,'rubber':1,'il_aleacion':1},True)
recipe('Machete','T05',{'steel':3,'metal':1,'il_mango':1,'rubber':1},True)
recipe('Bate de madera','T06',{'il_madera':3,'il_cinta':1})
recipe('Martillo','T06',{'iron':1,'metal':1,'il_mango':1})
recipe('Palanca · arma','T06',{'metal':3,'iron':1})
recipe('Llave inglesa','T06',{'iron':2,'metal':1})
recipe('Puño americano','T06',{'metal':2,'steel':1,'rubber':1},True)
recipe('Hacha','T07',{'iron':2,'metal':1,'il_mango':1,'rubber':1},True)
recipe('Hacha de combate','T07',{'steel':5,'metal':2,'il_mango':1,'rubber':2,'il_aleacion':1},True)
recipe('Hacha de piedra','T07',{},True,note='Reservada: cerrar receta y material pétreo coherente')
recipe('Portátil de acceso','T08',{'plastic':8,'il_circuito':3,'copper':6,'il_mecanismo':1},True,note='Casas aparcadas; reparar tras 3 usos satisfactorios')
recipe('Reparar portátil','T08',{'il_circuito':1,'copper':3,'plastic':2},note='Reparación del objeto existente; no crea otro portátil')
recipe('USB troyano','T08',{'plastic':2,'il_circuito':2,'copper':1},True,note='Consumible por intento')
recipe('Decodificador','T08',{'plastic':2,'il_circuito':2,'copper':3,'il_mecanismo':1},True)
recipe('Bote de spray','T09',{'plastic':3,'metalscrap':2})
recipe('Dispositivo de pinchos','T09',{'steel':2,'rubber':2,'il_pieza_coche':1},True)
recipe('Reparar pinchos','T09',{'steel':1,'rubber':1},note='Reparación; no genera un segundo dispositivo')
recipe('Placa de rol','T09',{'aluminum':4,'plastic':2,'il_cinta':1},True,note='Matrícula ficticia del juego; uso sujeto a la actividad')
recipe('Pistola SNS','T10',{'il_piezas_cortas':2,'steel':10,'metalscrap':8,'il_circuito':1},True)
recipe('Pistola','T10',{'il_piezas_cortas':3,'steel':16,'copper':8,'il_circuito':2},True)
recipe('Micro SMG','T11',{'il_piezas_compactas':4,'steel':24,'aluminum':12,'il_circuito':3,'il_aleacion':1},True,note='Reservada: origen de piezas compactas pendiente')
recipe('Munición 9 mm','T12',{'il_lote_municion':1,'copper':4,'steel':1},True,quantity=12,note='Lote de 12 unidades; validar identificador en inventario')

NPC_WEAPONS=[('Cuchillo',1500),('Bate de madera',2000),('Navaja automática',3200),('Daga',4200),('Machete',4500),('Hacha',3500),('Hacha de piedra',3000),('Hacha de combate',6500),('Martillo',1300),('Palanca · arma',2500),('Llave inglesa',2200),('Puño americano',3200),('Palo de golf',1000),('Taco de billar',800),('Botella',150)]

def validate():
 ids={r[0] for r in ROB}
 assert len(ids)==len(ROB)
 for r in ROB:
  if r[12]: assert sum(p for p,_ in r[12])==100, r[1]
 known={m[0] for m in MATERIALS}
 for r in RECIPES: assert set(r['parts'])<=known, r['name']
 assert len(TABLES)==12
 assert len(NPC_WEAPONS)+5==20
