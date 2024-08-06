from abc import ABC, abstractmethod

class APICallerInterface(ABC):
    @abstractmethod
    def get(self, prompt):
        pass
