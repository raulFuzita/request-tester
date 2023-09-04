from .idgenerator_interface import IDGenerator

class SequentialIDGenerator(IDGenerator):

    def __init__(self):
        self.current_id = 0

    def generate_id(self) -> str:
        self.current_id += 1
        return str(self.current_id)

    def set_starting_id(self, start_value: int):
        if start_value >= 0:
            self.current_id = start_value
        else:
            raise ValueError("Start value must be non-negative.")