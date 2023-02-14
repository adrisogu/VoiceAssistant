import webbrowser
import spotipy
import spotipy.util
import speech_recognition as sr
from spotipy.oauth2 import SpotifyClientCredentials
import pyttsx3
import pywhatkit


name = "Zara"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
rate= engine.getProperty("rate")                #Ajustando la velocidad 
engine.setProperty("rate", 135)
volume = engine.getProperty("volume")           #Ajustando el volumen
engine.setProperty("volume", 1)

#Autentificación para Spotify


#Función para reproducir un video de YouTube---
def talk(text):   
 engine.say(text)
 engine.runAndWait()

# Función para reconocer el audio 
def recognize():
    rec = None
    try:
        with sr.Microphone() as source:
            print("Escuchando..!")    
            talk("Dime que necesitas?")
            audio = listener.listen(source)
            rec = listener.recognize_google(audio, language="es-ES")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec    

def run_Zara():
    rec = recognize()
    if rec and 'reproduce' and 'YouTube' in rec:
        video_name = rec.replace("reproduce", '').strip()
        print("Reproduciendo " + video_name)
        talk("Reproduciendo " + video_name)
        pywhatkit.playonyt(video_name)
        


if __name__ == '__main__':
    run_Zara()    