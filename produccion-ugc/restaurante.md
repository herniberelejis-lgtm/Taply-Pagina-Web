# Pieza piloto UGC — restaurante, NFC + QR

Estado: preproducción. NO es un video renderizado. El acceso al proveedor de generación de video está pendiente.

Formato: vertical 9:16, 25 segundos. Dueño adulto de cafetería argentina, voz rioplatense natural, cámara de celular bien expuesta, piel real, sin apariencia de presentador publicitario. Referencia física: exhibidor blanco METRICSFIELD con NFC y QR; no sustituir por otra marca ni cambiar el diseño.

## Guion y montaje

0–6 s, dueño a cámara desde la barra: «Me decían que les encantaba el café. Pero después, la reseña quedaba para otro día». Tono honesto, no testimonio de resultados reales. Rótulo discreto: “Escena ilustrativa”.

6–12 s, interacción real: barista señala el exhibidor y cliente acerca lentamente el teléfono, lo mantiene un instante y mira la pantalla. Voz en off: «Ahora dejamos este acceso a mano, justo al terminar la visita».

12–19 s, detalle de manos: apertura de notificación NFC; cliente toca la notificación y llega a la página de reseñas. Voz: «Acercan un celular compatible, o escanean el QR, y pueden dejar su opinión». La interfaz se incorpora en posproducción, con perfil de demostración. No inventar una interfaz funcional dentro del render ni escanear el QR de referencia como si estuviera configurado.

19–25 s, dueño a cámara y corte al producto: «Menos pasos para ellos. Más fácil pedir una opinión real». Cierre: “NFC + QR para tu negocio”. No mostrar publicación automática, reseñas incentivadas, resultados garantizados ni beneficios económicos inventados.

## Prompts por toma

### A — dolor, 6 segundos
Vertical 9:16 photorealistic documentary UGC video, one continuous take. Realistic 35-year-old Argentine cafe owner in dark apron, medium close-up behind warm wood cafe counter, natural morning light, espresso machine in background. He looks into a handheld phone camera, speaks with subtle believable facial motion and small gestures, honest reflective tone, relaxed posture, real skin texture, no beauty filter. Argentine Spanish dialogue: “Me decían que les encantaba el café. Pero después, la reseña quedaba para otro día”. Do not rush speech; extend this shot if needed. No subtitles, no music, no invented on-screen logos.

### B — uso físico, 6 segundos
Animate from the approved reference frame. One continuous realistic handheld shot, preserve exact white NFC review standee and its printed design throughout. Female adult customer slowly moves the back of her black smartphone from 8cm away to 2cm above the NFC symbol, holds briefly, then gently withdraws phone to look at screen. Barista smiles naturally and points once with a small gesture. No morphing hands, no product deformation, no camera cuts, no floating interfaces, no magical auto-submission. Warm Argentine cafe, natural contact shadows, documentary realism. No dialogue needed; retain cafe ambience if supported.

### C — pantalla, 7 segundos
Over-the-shoulder closeup of an adult customer's real hand holding black smartphone at a cafe counter. Screen is an evenly lit neutral display for later screen replacement. Thumb makes one deliberate tap near top third of screen, then waits; no frantic tapping, no change of finger count, no distorted fingers, no warped screen. Stable phone geometry and planar screen, subtle camera sway, warm soft light. Do not generate readable UI or claim that a review is already published. Screen content will be composited in postproduction.

### D — beneficio, 6 segundos
Same owner and cafe as shot A, use approved identity reference, warm natural light, same wardrobe and counter. He looks at camera and says naturally in Argentine Spanish: “Menos pasos para ellos. Más fácil pedir una opinión real”. Small hand gesture toward exact white NFC standee. Gentle handheld camera movement, authentic expression, real skin, no dramatic corporate gestures, no subtitles, no generated overlays.

## Validación antes de entregar
- Producto consistente entre tomas y con las fotos del usuario.
- Teléfono, manos, contacto y miradas físicamente creíbles.
- Acción correcta: NFC abre una notificación/enlace; el cliente elige y publica su opinión.
- Voz argentina inteligible y sincronizada; no acelerar para forzar el guion.
- Si el proveedor no admite voz, generar voz por separado y sincronizar; no presentar un render silencioso como pieza final.
- No incorporar promesas de “+150 reseñas”, posiciones en Google ni calificaciones garantizadas.
- Ver la pieza completa, revisar continuidad y exportar MP4 H.264/AAC 1080×1920.

## Requisito pendiente
Acceso autorizado a un generador de video con capacidad de imagen a video y, para A y D, voz sincronizada o un flujo de sincronización labial. No hay API de video, credenciales utilizables ni GPU disponibles en el entorno actual. No se han realizado llamadas de video facturables.
