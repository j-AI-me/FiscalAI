# FiscalAI: Arquitectura General

Este documento resume la estructura propuesta para la aplicación **FiscalAI** según las indicaciones iniciales.

## 1. Frontend
- Formulario interactivo con React y Tailwind CSS (o Webflow con lógica condicional).
- Landing page con copy claro: "Descubre cómo pagar menos impuestos legalmente".
- Secciones destacadas: casos de éxito, testimonios y llamada a la acción (CTA) bien definida.

## 2. Backend y Lógica
- Procesamiento del formulario mediante **Node.js** o **Python FastAPI**.
- Motor de recomendación fiscal combinando modelos de lenguaje (OpenAI / GPT) y reglas lógicas personalizadas.
- Base de datos (PostgreSQL o Firebase) para almacenar respuestas y resultados.

### Salidas generadas
- Informe fiscal personalizado en formato PDF.
- Mapa societario recomendado.
- Timeline de acciones fiscales.
- Correo electrónico resumen con CTA a reunión.

## 3. Formulario Estructurado (Inputs)
1. **Identidad empresarial**: nombre de la empresa, estado (idea, operativa, en constitución), socios y participaciones.
2. **Estructura y actividad**: sector económico, modelo de negocio, facturación prevista, plantilla laboral, actividad internacional.
3. **Fiscalidad y estrategia**: tipo de tributación deseada (autónomo, SL, cooperativa...), búsqueda de inversores, deducciones posibles, interés en optimización avanzada.
4. **Datos operativos**: ubicación, software contable, auditoría.
5. **Perfil de riesgo y control**: inspecciones previas y nivel de riesgo asumible.

## 4. Sistema de Recomendación (Salidas Automáticas)
- Recomendación de tipo societario e impositivo.
- Deducciones fiscales e incentivos autonómicos/estatales.
- Avisos de cumplimiento obligatorio (facturación electrónica, etc.).
- Propuesta de calendario fiscal.

## 5. Marketing Integrado
- Hook inicial: "Completa esto y recibe un plan fiscal gratuito personalizado".
- Informe PDF con branding y CTA para reservar sesión con un experto.
- Automatización de mensajes:
  - Día 0: entrega del informe.
  - Día 2: caso similar + vídeo explicativo.
  - Día 5: recordatorio de cambios normativos y nuevos incentivos.

