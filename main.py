from interface.listeners.input_listener import InputListener
from infrastructure.api.api_caller import APICaller
from infrastructure.stt.stt_module import STTModule
from infrastructure.tts.tts_module_free import TTSModuleFREE
from domain.services.command_service import CommandService
from application.use_cases.process_command import ProcessCommand

if __name__ == "__main__":
    api_caller = APICaller()
    tts_module = TTSModuleFREE()
    command_service = CommandService(api_caller, tts_module)
    process_command_use_case = ProcessCommand(command_service)

    stt_module = STTModule()
    input_listener = InputListener(stt_module, process_command_use_case)
    input_listener.start()
