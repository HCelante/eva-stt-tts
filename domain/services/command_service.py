class CommandService:
    def __init__(self, api_caller, tts_module):
        self.api_caller = api_caller
        self.tts_module = tts_module

    def process_command(self, command):
        response = self.api_caller.get(command.text + ' em 1 tweet curto sem #')
        self.tts_module.speak(response)
        return response
