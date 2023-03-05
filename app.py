import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia as wk
import pywhatkit as pw
import webbrowser


audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():

    try:
        with sr.Microphone(1) as mic:
            # Chama o algortmo de redução de ruidos no som
            audio.adjust_for_ambient_noise(mic)
            texto_inicial = 'Em que posso ajudar'
            maquina.say(texto_inicial)
            maquina.runAndWait()
            #print("O que você precisa?")
            # lista os microfones utilizandos
            #print(sr.Microphone().list_microphone_names())
            
            voz = audio.listen(mic)
            
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            
            
            if 'Lisa' in comando:
                comando = comando.replace('Lisa', '')
                voices = maquina.setProperty('voices')
                maquina.setProperty('voice', voices[0].id)
                maquina.setProperty('rate', 160)
                maquina.runAndWait()       
                print('Você disse: ' + comando)
    except sr.UnknownValueError:
        print('Microfone não esta OK')
        
    return comando
    
    
def horas():
    hora = datetime.now().strftime('%H:%M')
    print(hora)
    return hora
    
def comando_voz_usuario():
    comando = executa_comando()
    
    if 'horas' in comando:
        maquina.say('Agora são' + horas())
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
    elif 'navegador' in comando:
        resultado = webbrowser.open('https://google.com.br')
        maquina.say('Abrindo o navegador')
        maquina.runAndWait()
    else:
        print('Não entendi!')
        
        
               
        
        
        
comando_voz_usuario()