import threading
from queue import Queue
from pynput import keyboard
from domain.entities.command import Command
from domain.services.command_service import CommandService
from application.use_cases.process_command import ProcessCommand
from infrastructure.stt.stt_module import STTModule

class InputListener(threading.Thread):
    def __init__(self, stt_module, process_command_use_case):
        super().__init__()
        self.stt_module = stt_module
        self.process_command_use_case = process_command_use_case
        self.command_queue = Queue()
        self.response_queue = Queue()
        self.listening = True
        self.lock = threading.Lock()

    def capture_audio(self):
        while self.listening:
            comando = self.stt_module.capture_audio()
            if comando:
                print(f"Comando capturado: {comando}")
                self.command_queue.put(Command(comando))

    def process_commands(self):
        while self.listening:
            command = self.command_queue.get()
            if command:
                print(f"Processando comando: {command.text}")
                response = self.process_command_use_case.execute(command)
                self.response_queue.put(response)

    def play_responses(self):
        while self.listening:
            response = self.response_queue.get()
            if response:
                print(f"Tocando resposta: {response}")

    def run(self):
        audio_thread = threading.Thread(target=self.capture_audio)
        command_thread = threading.Thread(target=self.process_commands)
        response_thread = threading.Thread(target=self.play_responses)

        audio_thread.start()
        command_thread.start()
        response_thread.start()

        audio_thread.join()
        command_thread.join()
        response_thread.join()
