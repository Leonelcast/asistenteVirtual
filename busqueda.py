import wikipedia
import speech_recognition as speech
import pyttsx3

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
    talk("¿Qué busqueda quieres realizar?")
    grabar = listen()
    pregunta = grabar
    wikipedia.set_lang("es")
    res = wikipedia.summary(pregunta, sentences = 2)
    talk(res)

escuchar()