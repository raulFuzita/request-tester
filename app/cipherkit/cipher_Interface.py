from abc import ABC, abstractmethod

class CipherInterface(ABC):
    @abstractmethod
    def encrypt(self, data: str) -> str:
        pass
    
    @abstractmethod
    def validate(self, encrypted_data: str, validation_data: str) -> bool:
        pass