# Importar librerias
from tkinter import *
from gtts import gTTS
import os
import pygame
import time
from datetime import datetime

# Se inicializa el pygame mixer
pygame.mixer.init()

# Funcion para convertir el texto a Speech
def preview_text_to_speech():
    
    # Se elimina el archivo temporal si existe 
    if os.path.exists("temp_preview.mp3"):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()  # Unload para liberar el archivo

        time.sleep(0.5)  # Tiempo de espera para liberar el archivo
        os.remove("temp_preview.mp3")

    # get el string del usuario
    text = text_entry.get("1.0", END).strip()
    
    # Definir el idioma del speech
    language = "es"
    
    # Convertir el texto a speech con un acento de mexico
    speech = gTTS(text=text, lang=language, slow=False, tld="com.mx")  
    
    # Guardar el archivo como mp3
    speech.save("temp_preview.mp3")

    # Reproducir el archivo temporal de audio
    pygame.mixer.music.load("temp_preview.mp3")
    pygame.mixer.music.play()
    
    # Estatus de guardado
    status_label.config(text="Reproduciendo el texto convertido a voz...")

# Funcion para guardar el audio 
def save_text_to_speech():
    # Ver si existe un archivo temporal
    if os.path.exists("temp_preview.mp3"):
        #Liberar el archivo de audio
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()  # Unload para liberar el archivo
        time.sleep(0.5)  # Tiempo de espera para liberar el archivo

        #Dia en que se guarda el archivo
        now = datetime.now() # current date and time
        date_time = now.strftime("%d")  #dia
        date_time+= now.strftime("%m")  #mes
        date_time+= now.strftime("%M")  #minuto
        date_time+= now.strftime("%S")  #segundo
        
        # Renombrar el archivo temporal
        os.rename("temp_preview.mp3", "audioTexto_"+date_time+".mp3")
        status_label.config(text="¡El archivo de audio ha sido guardado como output_audio.mp3!")
    else:
        status_label.config(text="Por favor, escucha una vista previa antes de guardar.")

# Funcion para cerrar la ventana y eliminar archivos temporales
def on_closing():

    # Remover archivo temporal si existe
    if os.path.exists("temp_preview.mp3"):
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        os.remove("temp_preview.mp3")

    # Cerrar la ventana
    window.destroy()

# Instanciar la ventana
window = Tk()
window.title("Texto a Voz (Spanish)")   #Titulo de la ventana emergente
window.geometry("400x350")  #Tamaño de la ventana emergente

# Crear y acomodar label, ventana y boton en la ventana emergente
Label(window, text="Introduce el texto para convertir a voz:").pack(pady=10)
text_entry = Text(window, height=10, width=40)
text_entry.pack(pady=10)

# Button para la prueba de text-to-speech
preview_button = Button(window, text="Escuchar vista previa", command=preview_text_to_speech)
preview_button.pack(pady=10)

# Button para guardar el audio
save_button = Button(window, text="Guardar archivo de audio", command=save_text_to_speech)
save_button.pack(pady=10)

status_label = Label(window, text="")
status_label.pack(pady=10)

# Escuchador en el boton de cerrado
window.protocol("WM_DELETE_WINDOW", on_closing)

# Ejecutar en un loop
window.mainloop()