# Texo_a_Audio
Este proyecto es una aplicación de Python que convierte texto a voz (TTS - Text to Speech) en español utilizando la biblioteca gTTS (Google Text-to-Speech).
La aplicación incluye una interfaz gráfica de usuario (GUI) creada con Tkinter, donde los usuarios pueden introducir texto, escuchar una vista previa de la conversión de texto a voz, y luego decidir si desean guardar el archivo de audio resultante.

## Funcionalidades
- Conversión de texto a voz: Permite a los usuarios ingresar texto en español y generar una vista previa del archivo de audio.
- Reproducción de vista previa: Los usuarios pueden escuchar la conversión antes de decidir si guardan el archivo.
- Guardar archivo de audio: Una vez que se haya escuchado la vista previa, los usuarios pueden guardar el archivo de audio como un archivo .mp3 con un nombre único basado en la fecha y hora actual.
- Limpieza automática: Se elimina cualquier archivo temporal una vez que se cierra la aplicación.

## Requisitos
Para ejecutar este proyecto, necesitas instalar las siguientes bibliotecas de Python:

  1. gTTS (Google Text-to-Speech)
  2. pygame (para reproducir el audio)
  3. Tkinter (incluido con la mayoría de las instalaciones de Python)

## Instrucciones de Uso
- Al ejecutar el programa, se abrirá una ventana donde puedes introducir el texto que deseas convertir a voz.

- Haz clic en el botón Escuchar vista previa para generar y escuchar una vista previa del archivo de audio.

- Si estás satisfecho con la vista previa, haz clic en Guardar archivo de audio para guardar el archivo como un archivo .mp3 en tu carpeta de trabajo.

- El archivo se guardará con un nombre basado en la fecha y hora, por ejemplo: audioTexto_25091235.mp3.

- Cuando cierres la aplicación, cualquier archivo temporal se eliminará automáticamente.

## Ejemplo de Uso

1. Introduce el texto en la caja de texto.
2. Escucha una vista previa.
3. Guarda el archivo si estás satisfecho con el resultado.
