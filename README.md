# Sistema ilegal · SIEGA Community

Web pública en español para consultar el funcionamiento y las normas del sistema ilegal de SIEGA Community. Es una web estática de HTML, CSS, JavaScript y SVG, con tipografías locales y sin dependencias de compilación.

## Contenido

- `index.html`: sitio navegable y adaptable a escritorio y móvil.
- `content/normativa.md`: normativa pública en revisión.
- `content/guia.md`: guía para participantes.
- `assets/`: estilos, scripts, ilustraciones y fuentes con licencias OFL.

La web solo publica información destinada a jugadores. No incluye recetas, cantidades de botín, precios ni procedimientos internos de coordinación. Que una actividad aparezca como pendiente no significa que esté habilitada en el servidor. La normativa y la guía son borradores hasta su aprobación y publicación oficial.

## Vista previa local

Desde esta carpeta, inicia un servidor estático (por ejemplo, `python -m http.server 8765`) y abre `http://127.0.0.1:8765/`. No abras el HTML mediante `file://`, porque la página carga los documentos Markdown con `fetch`.

## Publicación

El flujo `.github/workflows/pages.yml` publica automáticamente el sitio en GitHub Pages cuando hay un cambio en la rama `main` o se ejecuta manualmente desde Actions. Para este repositorio, configura una vez **Settings → Pages → Build and deployment → GitHub Actions**. Después de cada `push` a `main`, la acción **Publicar sitio** despliega la web.

## Mantenimiento

Al aprobar cambios, actualiza los documentos y su estado/fecha de revisión en la misma entrega. Las fuentes Space Grotesk y DM Sans están incluidas localmente junto con sus licencias OFL.
