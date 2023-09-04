from sqlalchemy.orm import DeclarativeBase
from typing import Type, Generic, TypeVar
from sqlalchemy import update
from ...dbconnector.db_connector_manager import DatabaseConnectionManager

T = TypeVar('T', bound=DeclarativeBase)

class RepositoryDAO(Generic[T]):
    def __init__(self, connection_manager: DatabaseConnectionManager, model: Type[T]):
        self.connection_manager = connection_manager
        self.model = model

    def _get_session(self):
        return self.connection_manager.get_session()
        
    def add(self, cls: T):
        session = self._get_session()
        session.add(cls)
        session.commit()
        return cls.id

    def get_by_id(self, cls_id: int) -> T:
        session = self._get_session()
        return session.query(self.model).filter(self.model.id == cls_id).first()

    def get_all(self):
        session = self._get_session()
        return session.query(self.model).all()

    def update(self, cls: T):
        session = self._get_session()
        cls_dict = cls.to_dict(include_relationships=False)
        print(cls_dict)  # Debug output here
        stmt = (
            update(self.model)
            .where(self.model.id == cls.id)
            .values(**cls_dict)
        )
        session.execute(stmt)
        session.commit()

    def delete(self, cls_id: int):
        session = self._get_session()
        cls = session.query(self.model).filter(self.model.id == cls_id).first()
        if cls:
            session.delete(cls)
            session.commit()

    def _check_type(self, cls: T):
        if not issubclass(cls, DeclarativeBase):
            raise TypeError(f"{cls.__name__} must be a subclass of DeclarativeBase")