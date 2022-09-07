from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import speech_recognition as speech
import pyttsx3, pywhatkit

CLIENT_FILE = "secret.json"
API_NAME = "gmail"
API_VERSION = "v1"
SCOPES = ["https://mail.google.com/"]

service = Create_Service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)

oyente = speech.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[3].id)


mimeMessage = MIMEMultipart()
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


def envioCorreo():
    talk("¿Deseas enviar un correo?")
    grabar = listen()
    print(grabar)
    if "sí" in grabar:
        print("Para quien es el correo? ")
        talk("¿Para quien es el correo?")
        capturarvoz = listen()
        n = capturarvoz.replace("ñ", "n")
        sin_espacio = n.replace(" ", "")
        global correo 
        correo = sin_espacio + "@unis.edu.gt"
        print(sin_espacio + "@unis.edu.gt")
        print("¿Cual es el asunto del correo?")
        talk("¿Cual es el asunto del correo?")
        asunto = listen()
        global titulo_asunto
        titulo_asunto = asunto
        print("¿Cual es la descripcion del correo?")
        talk("¿Cual es la descripcion del correo?")
        descripcion = listen()
        global descripcion_correo
        descripcion_correo = descripcion 
        enviar_correo()

def enviar_correo():
    talk("¿Desea enviar el correo?")
    capturarvoz = listen()
    if "sí" in capturarvoz:
        mimeMessage["to"] = correo
        mimeMessage["subject"] = titulo_asunto
        emailMsg = descripcion_correo 
        mimeMessage.attach(MIMEText(emailMsg, "plain"))
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId = "me", body = {"raw": raw_string}).execute()
        print("Se ha enviado el correo")
        talk("Se ha enviado el correo")
    else:
        pass 

if __name__ == "__main__":
    envioCorreo()