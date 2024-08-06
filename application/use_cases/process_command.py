class ProcessCommand:
    def __init__(self, command_service):
        self.command_service = command_service

    def execute(self, command):
        return self.command_service.process_command(command)
