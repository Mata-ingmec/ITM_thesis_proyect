import speech_recognition as sr
import pyautogui

recognizer = sr.Recognizer()
proceso = None

def ejecutar_comando(comando):
    print(comando) 

def escuchar_comandos():
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-MX")
        print(f"Comando reconocido: {comando}")
        ejecutar_comando(comando)
    except sr.UnknownValueError:
        print("No se pudo entender el comando.")
    except sr.RequestError as e:
        print(f"Error al realizar la solicitud: {e}")

while True:
    escuchar_comandos()