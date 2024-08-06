import speech_recognition as sr
from domain.interfaces.stt_interface import STTInterface

class STTModule(STTInterface):
    def __init__(self):
        self.microfone = sr.Recognizer()

    def capture_audio(self):    
        try:
            with sr.Microphone() as source:
                print('Eva está te escutando...')
                audio_capturado = self.microfone.listen(source, timeout=5, phrase_time_limit=5)
                print('Áudio capturado, processando...')
                comando_reconhecido = self.microfone.recognize_google(audio_capturado, language='pt-BR')
                comando_reconhecido = comando_reconhecido.lower()
                print("Comando capturado: " + comando_reconhecido)
                return comando_reconhecido
        except sr.UnknownValueError:
            print('Não foi possível te entender. Diga novamente...')
            return ""
        except sr.RequestError as e:
            print(f'Erro de requisição com o serviço de reconhecimento de fala: {e}. Tentando novamente...')
            return ""
        except Exception as err:
            print('Erro inesperado ao capturar o áudio.')
            print(err)
            return ""
