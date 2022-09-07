import webbrowser
import pyautogui
from time import sleep

import speech_recognition as speech
import pyttsx3, pywhatkit


oyente = speech.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

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

def iniciar():
    
    talk("¿Qué quieres hacer alarma, cronometro o temporizador?")
    grabar = listen()

    print(grabar)
    if "alarma" in grabar:
        webbrowser.open("https://www.temporizadoronline.com/despertador/")
        sleep(3)
        for i in range(22):
            pyautogui.press("tab")
        sleep(2)
        talk("¿Hora en formato de 24 horas?")
        horas = listen()
        print(horas)
        for i in range(int(horas)):
            pyautogui.press("enter")
        talk("¡Deseas agregarle minutos?")
        grabar = listen()
        print(grabar)
        if "sí" in grabar:
            for i in range(2):
                pyautogui.press("tab")
            talk("¿Minutos?")
            minutos = listen()
            print(minutos)
            for i in range(int(minutos)):
                pyautogui.press("enter")
            for i in range(2):
                pyautogui.press("tab")
            pyautogui.press("enter")
        elif "no" in grabar:
            for i in range(4):
                pyautogui.press("tab")
            pyautogui.press("enter")
        
    if "cronómetro" in grabar:
        webbrowser.open("https://www.temporizadoronline.com/cronometro/") 
        sleep(3)
        for i in range(6):
            pyautogui.press("tab")
        pyautogui.press("enter")
    
    if "temporizador" in grabar:
        webbrowser.open("https://www.temporizadoronline.com/")
        sleep(3)
        talk("¿Temporizador en hora, minutos o segundos?")
        grabar = listen()
        print(grabar)
        if "hora" in grabar:
            print(grabar)
            for i in range(18):
                pyautogui.press("tab")
            sleep(2)
            talk("¿Cuantas horas le asignaras al temporizador?")
            horas = listen()
            print(horas)
            for i in range(int(horas)):
                pyautogui.press("enter")
            for i in range(6):
                pyautogui.press("tab")
            pyautogui.press("enter")
        
        elif "minuto" in grabar:
            print(grabar)
            for i in range(20):
                pyautogui.press("tab")
            sleep(2)
            talk("¿Cuantos minutos le asignaras al temporizador?")
            minutos = listen()
            print(minutos)
            for i in range(int(minutos)):
                pyautogui.press("enter")
            for i in range(4):
                pyautogui.press("tab")
            pyautogui.press("enter")

        elif "segundo" in grabar:
            print(grabar)
            for i in range(22):
                pyautogui.press("tab")
            sleep(2)
            talk("¿Cuantos segundos le asignaras al temporizador?")
            minutos = listen()
            print(minutos)
            for i in range(int(minutos)):
                pyautogui.press("enter")
            for i in range(2):
                pyautogui.press("tab")
            pyautogui.press("enter")

   
           

iniciar()