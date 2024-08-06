import pygame
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment, effects

class TTSModuleFREE:
    def __init__(self):
        pass

    def speak(self, command):
        try:
            tts = gTTS(text=command, lang='pt-br')

            buffer = BytesIO()
            tts.write_to_fp(buffer)
            buffer.seek(0)

            audio = AudioSegment.from_file(buffer, format="mp3")
            audio = audio.speedup(playback_speed=1.3)
            audio = effects.normalize(audio)

            buffer = BytesIO()
            audio.export(buffer, format="mp3")
            buffer.seek(0)

            pygame.mixer.init()
            pygame.mixer.music.load(buffer)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as err:
            print('Erro no serviço de TTS gTTS da Google')
            print(err)
        finally:
            pygame.mixer.quit()
