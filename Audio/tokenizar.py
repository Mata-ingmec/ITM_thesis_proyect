import re                                   # Manejo de expresiones regulares
import nltk                                 # Para procesar lenguaje natural
from nltk.tokenize import word_tokenize     # Para Tokenizar un texto
from nltk.corpus import stopwords           # Cargar las"Stopwords" del espaÃ±ol  
nltk.download('punkt')
nltk.download('stopwordscle')
import speech_recognition as sr

voz = sr.Recognizer()

with sr.AudioFile('C:\\Users\\mata_\\OneDrive\\Escritorio\\Maestría\\Audio\\consulta.wav') as source:
    audio = voz.listen(source)
    try: 
        print("Convirtiendo archivo de audio en texto...")
        texto = voz.recognize_google(audio, language='es-MX')
    except:
        print("Hubo un error, no se pudo traducir, vuelva a intentar.")    

print("\nTexto Completo:\n\n", texto)
texto_sin_simbolos = re.sub(r'[^\w\s]', '', texto)
tokens_de_mi_texto = word_tokenize(texto_sin_simbolos)
print('\n Tokens Totales: ', len(tokens_de_mi_texto))
palabras_vacias = set(stopwords.words('spanish'))
lista_palabras = []
for palabra in tokens_de_mi_texto:
    if palabra not in palabras_vacias:
        lista_palabras.append(palabra)
print(lista_palabras)
contador = []
lista_final=[]
for i in range(len(lista_palabras)):
    if lista_palabras[i] not in lista_final:
        lista_final.append(lista_palabras[i])
print(lista_final)
for i in range(len(lista_final)):
    rep = lista_palabras.count(lista_final[i])
    contador.append(rep)
print(contador)