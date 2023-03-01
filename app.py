import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia as wk
import pywhatkit as pw


audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():

    try:
        with sr.Microphone() as source:
            print("Ouvindo...")

            voz = audio.listen(source)
            
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            
            if 'cleiton' in comando:
                comando = comando.replace('cleiton', '')
                #maquina.say(comando)
                maquina.runAndWait()       
                print(comando)
    except:
        print('Microfone não esta OK')
        
    return comando
    
    
def comando_voz_usuario():
    comando = executa_comando()
    
    if 'horas' in comando:
        hora = datetime.now().strftime('%H%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wk.set_lang('pt')
        resultado = wk.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pw.playonyt(musica)
        maquina.say('Tocando musica')
        maquina.runAndWait()
        
        
        
        
comando_voz_usuario()