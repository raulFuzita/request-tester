from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import DateTime

class BaseDTO(DeclarativeBase):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, onupdate=func.now(), default=func.now())

    def to_dict(self, include_relationships=False):
        raise NotImplementedError("to_dict method must be implemented")
