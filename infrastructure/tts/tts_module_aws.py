import pygame
import boto3
import os
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

class TTSModuleAWS:
    def __init__(self):
        self.secret_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.database_url = os.getenv("AWS_SECRET_ACCESS_KEY")

    def speak(self, command):
        try:
            polly_client = boto3.Session(
                aws_access_key_id=self.secret_key,
                aws_secret_access_key=self.database_url,
                region_name='us-west-2'
            ).client('polly')

            response = polly_client.synthesize_speech(
                Text=command,
                OutputFormat='mp3',
                VoiceId='Camila'
            )

            with open('speech.mp3', 'wb') as file:
                file.write(response['AudioStream'].read())

            pygame.mixer.init()
            pygame.mixer.music.load('speech.mp3')
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as err:
            print('Erro no serviço de TTS Polly da AWS')
            print(err)
