import speech_recognition as sr
import pyttsx3

# Inicializa o objeto de reconhecimento de fala
r = sr.Recognizer()

# Inicializa o objeto de síntese de voz
engine = pyttsx3.init()

# Configurações da voz do sistema
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

# Função que converte o áudio em texto e executa uma ação com base no comando do usuário
def run_command(command):
    if "Ligar luz" in command:
        # Coloque aqui o código para ligar a luz
        print("Tudo bem! Ligando luz agora mesmo...")
        engine.say("Tudo bem! Ligando luz agora mesmo...")
    elif "Desligar luz" in command:
        # Coloque aqui o código para desligar a luz
        print("Tudo bem! Desligando luz agora mesmo...")
        engine.say("udo bem! Desligando luz agora mesmo...")
    else:
        print("Comando não válido")
        print(command)
        engine.say("Desculpe, não entendi o que você disse.")

    engine.runAndWait()

# Captura a entrada de áudio do usuário
with sr.Microphone() as source:
    print("Diga algo!")
    audio = r.listen(source)

    try:
        # Usa o objeto de reconhecimento de fala para converter o áudio em texto
        command = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + command)

        # Executa uma ação com base no comando do usuário
        run_command(command)
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError as e:
        print("Não foi possível completar a solicitação. {0}".format(e))