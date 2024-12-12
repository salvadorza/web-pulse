# web-pulse
Web Pulse es una herramienta interactiva creada con Tkinter que verifica la conectividad de un sitio web introducido por el usuario. Permite ingresar una URL, valida si está activa o no, y muestra el resultado visualmente en un canvas. Ideal para comprobar rápidamente el estado de una página web.

# Características🔥

● Interfaz Gráfica de Usuario (GUI): Diseñada con Tkinter, incluye un campo de entrada, botones y un canvas para resultados visuales.

● Validación Automática de URLs: Si la URL no incluye https, el programa lo agrega automáticamente para evitar errores.

● Indicador de Estado: Verifica si un sitio web está activo (HTTP 200 OK) o inactivo, mostrando mensajes claros.

● Feedback Visual: Los resultados se muestran con texto en colores: verde para sitios activos y rojo para errores o sitios inactivos.

● Gestión de Errores: Maneja excepciones y muestra mensajes cuando la URL no es válida o si ocurre un problema durante la conexión.

● Selección Rápida de Texto: Permite seleccionar todo el contenido del campo de entrada usando Ctrl+A para facilitar la edición.

● Compatibilidad Dinámica: Se adapta a diferentes resoluciones gracias al diseño con dimensiones relativas en su interfaz.

# Requisitos🔎

Tener Python instalado.

Librerías usadas:

● Tkinter

● urllib.request
