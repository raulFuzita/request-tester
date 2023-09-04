from abc import ABC, abstractmethod

class IDGenerator(ABC):

    @abstractmethod
    def generate_id(self) -> str:
        """
        Generate a new unique ID.
        :return: Unique ID as string.
        """
        pass

    @abstractmethod
    def set_starting_id(self, start_value: int):
        """
        Set the starting value for ID generation.
        :param start_value: The value from which to start ID generation.
        """
        pass


