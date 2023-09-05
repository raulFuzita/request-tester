from .idgenerator_interface import IDGenerator
import uuid

class UUIDGenerator(IDGenerator):

    def generate_id(self) -> str:
        """
        Generate a new unique UUID.
        :return: UUID as string.
        """
        return str(uuid.uuid4())

    def set_starting_id(self, start_value: int):
        """
        This method does not make sense for UUIDs as they are not sequential.
        Calling this will raise a NotImplementedError.
        """
        raise NotImplementedError("Cannot set a starting value for UUIDs.")