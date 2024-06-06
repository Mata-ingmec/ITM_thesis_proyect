import mysql.connector as mc
import speech_recognition as sr
import pyautogui

lista = ["diabetes", "glucosa", "necrosis", "fatiga", "enfermedad", "antecedentes"]
db = mc.connect(user='root', password='pichi159', host='localhost', database = 'audio', port='3306')

#Configuración de micrófono --------------------------------------------
recognizer = sr.Recognizer()
proceso = None

def ejecutar_comando(comando):
    comando.lower()
    if "agregar" in comando:
        for palabra in lista:
            if palabra in comando:
                resultado = palabra
                print("Se ejecutará INSERT")
                cur = db.cursor()
                cur.execute('INSERT INTO prueba_db (listado) VALUES (%s)', (resultado,))
                db.commit()
    elif "cambiar" in comando:
        for palabra in lista:
            if palabra in comando:
                resultado = palabra
                for cambio in lista:
                    if cambio in comando and cambio != resultado:
                        print("Se ejecutará UPDATE")
                        cur = db.cursor()
                        cur.execute('UPDATE prueba_db SET listado = %s WHERE listado = (%s)', (cambio, resultado))
                        db.commit()

    elif "borrar" in comando:
        for palabra in lista:
            if palabra in comando:
                resultado = palabra
                print("Se ejecutará DELETE")
                cur = db.cursor()
                cur.execute('DELETE FROM prueba_db WHERE listado = %s', (resultado,))
                db.commit()

def insertar_comando(comando):
    comando.lower()
    if "agregar" in comando:
        instruccion = "INSERT"
        for palabra in lista:
            if palabra in comando:
                resultado = palabra
                print("Se ejecutará INSERT")
                cur = db.cursor()
                cur.execute('INSERT INTO palabras (instruccion, resultado) VALUES (%s, %s)', (instruccion, resultado))
                db.commit()
    elif "cambiar" in comando:
        instruccion = "UPDATE"
        for palabra in lista:
            if palabra in comando:
                resultado = palabra
                print("Se ejecutará UPDATE")
                cur = db.cursor()
                cur.execute('INSERT INTO palabras (instruccion, resultado) VALUES (%s, %s)', (instruccion, resultado))
                db.commit()
    elif "borrar" in comando:
        instruccion = "DELETE"
        for palabra in lista:
            if palabra in comando:
                resultado = palabra
                print("Se ejecutará DELETE")
                cur = db.cursor()
                cur.execute('INSERT INTO palabras (instruccion, resultado) VALUES (%s, %s)', (instruccion, resultado))
                db.commit()
    elif "mostrar" in comando or "Mostrar" in comando:
        instruccion = "SELECT"
        for palabra in lista:
            if palabra in comando:
                resultado = palabra
                print("Se ejecutará SELECT")
                cur = db.cursor()
                cur.execute('INSERT INTO palabras (instruccion, resultado) VALUES (%s, %s)', (instruccion, resultado))
                db.commit()

def escuchar_comandos():
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language="es-MX")
        print(f"Comando reconocido: {comando}")
        insertar_comando(comando)
        ejecutar_comando(comando)
    except sr.UnknownValueError:
        print("No se pudo entender el comando.")
    except sr.RequestError as e:
        print(f"Error al realizar la solicitud: {e}")

while True:
    escuchar_comandos()
