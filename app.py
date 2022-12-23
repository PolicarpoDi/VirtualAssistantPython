import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('Fala meu patrão')
maquina.say('Eu sou o Cleiton')
maquina.say('como posso ajudar?')
maquina.runAndWait()



try:
    with sr.Microphone() as source:
        print("Ouvindo...")
        voz = audio.listen(source)
        
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
        if 'cleiton' in comando:
            print(comando)
            
except:
    print('Microfone não esta OK')