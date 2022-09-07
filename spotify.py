import speech_recognition as speech
import pyttsx3, pywhatkit
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
#Libreria para abrir internet
import webbrowser 
#libreria para manejar el ordenador
import pyautogui
from time import sleep




client_id = "4fbc5e8386b24d9d838bc3281c0cd2b1"
client_secret = "583aae1a43aa457aa247cd80321657a3"
error_nombre_cancion = 0
artista = ''
cancion = ''    

oyente = speech.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[3].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with speech.Microphone() as source:
            print("Escuchando...")
            pc = oyente.listen(source)
            grabar = oyente.recognize_google(pc, language='es-ES')
            grabar = grabar.lower(0)          
               

    except:
        pass
    return grabar

def escuchar():
    talk("¿Busqueda por artista o cancion?")
    grabar = listen()
    print(grabar)
    if "canción" in grabar:
        reproducir_cancion()
    if "artista" in grabar:
        random_artista()
    else: 
        pass


def reproducir_cancion():
    global cancion
    talk("¿Qué canción deseas reproducir?")
    grabar = listen()
    if "" in grabar:
        cancion = grabar.upper()
        iniciar()

    else: 
        pass

def random_artista():
    global artista
    talk("¿Qué artista deseas reproducir?")
    grabar = listen()
    if "" in grabar:
        artista = grabar.upper()
        iniciar_artista()

    else: 
        pass

def iniciar():
    global error_nombre_cancion
    global cancion

    if len(artista) > 0:

        spotify_cred = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
        result = spotify_cred.search(artista)

        for i in range(0, len(result["tracks"]["items"])):
            nombre_cancion = result["tracks"]["items"][i]["name"].upper()

            if cancion in nombre_cancion:
                error_nombre_cancion = 1
                webbrowser.open(result["tracks"]["items"][i]["uri"])
                sleep(5)
                pyautogui.press("enter")
                break
                         
            
    if error_nombre_cancion == 0:
        cancion = cancion.replace(" ", "%20")
        webbrowser.open(f'spotify:search:{cancion}')
        sleep(6)
        for i in range(4):
        #for i in range(24):                
            pyautogui.press("tab")
        pyautogui.press("enter")
        
      
     
def iniciar_artista():
    global error_nombre_cancion
    global cancion
    global artista
    spotify_cred = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    result = spotify_cred.search(artista)
    for i in range(0, len(result["tracks"]["items"])):
        nombre_cancion = result["tracks"]["items"][i]["name"].upper()
        if cancion in nombre_cancion:
            error_nombre_cancion = 1
            webbrowser.open(result["tracks"]["items"][i]["uri"])
            pyautogui.press("enter")
            break
                           
     

escuchar()