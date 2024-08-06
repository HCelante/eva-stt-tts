from abc import ABC, abstractmethod

class STTInterface(ABC):
    @abstractmethod
    def capture_audio(self):
        pass
