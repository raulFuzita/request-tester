from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import DateTime
import datetime

class BaseDTO(DeclarativeBase):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, onupdate=datetime.datetime.now, default=func.now())
