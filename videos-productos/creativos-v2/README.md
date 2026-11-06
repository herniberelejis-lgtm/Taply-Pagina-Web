# Borradores de video — revisión con master playbook

- [Sticker — El atajo (28 s)](01-sticker-el-atajo.mp4)
- [Tarjeta — No es para pagar (24 s)](02-tarjeta-no-es-para-pagar.mp4)

Se utilizó HyperFrames, siguiendo la skill del proyecto HeyGen y el master playbook aportado por el usuario. Las piezas usan enfoques distintos a los personajes del video de referencia: olvido/notificaciones y expectativa de tarjeta bancaria.

Ambos archivos: 1080 × 1920, 30 fps, MP4 H.264/AAC. Con animaciones, tipografía grande, imágenes de producto de la biblioteca del usuario y música sintética propia retimada. Sin locución. Composiciones verificadas con cero errores y cero advertencias. Ambos MP4 se decodificaron completos y se verificaron sus metadatos. El sonido fue medido, no escuchado.

Reglas aplicadas: marca MetricsField Reviews; toque distinto de reseña; mismo enlace público para todos; el cliente escribe y publica; interacciones por día, hora y pieza; sin cifras, capturas ni datos de comercios; sin promesas de rendimiento, precios, pruebas ni Loyalty. CTA de elección del producto para Mercado Libre; no se usó Comentá DEMO, que corresponde a Instagram.

Son borradores para revisión humana; no se publicó ninguna campaña. Los assets de teléfono son instrucciones ilustrativas, no una captura del software. No se presentó como real una pantalla del panel que no se tiene.

Cada carpeta contiene la fuente HyperFrames editable. Requiere Node 22+, Chromium y FFmpeg. CLI fijada en package.json: `npm install`, `npm run check`, `npm run dev`, `npm run render`.

Skill aplicada: https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/SKILL.md
