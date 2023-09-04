from .command_interface import Command
from app.model.dto.base import BaseDTO
from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True)

class RequiredTablesCommand(Command):

    def execute(self) -> bool:
        BaseDTO.metadata.create_all(engine)
        return True