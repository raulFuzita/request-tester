from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..model.dto.base import BaseDTO
from ..idgenerator.uuid_id import UUIDGenerator
import threading

uuid_generator = UUIDGenerator()

class DatabaseConnectionManager:
    def __init__(self, db_url, pool_size=10, max_overflow=20):
        if "sqlite" in db_url:
            self.engine = create_engine(db_url)
        else:
            self.engine = create_engine(db_url, pool_size=pool_size, max_overflow=max_overflow)
        self.Session = sessionmaker(bind=self.engine)
        self.local = threading.local()
        BaseDTO.metadata.create_all(self.engine)
        self.id = uuid_generator.generate_id()
        print(f"DatabaseConnectionManager({self.id}) created")

    def get_session(self):
        if not hasattr(self.local, "session"):
            self.local.session = self.Session()
        return self.local.session

    def close_session(self):
        if hasattr(self.local, "session"):
            self.local.session.close()
            self.local.session = None

    def __enter__(self):
        return self.get_session()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_session()

    def __repr__(self) -> str:
        return f"DatabaseConnectionManager({self.id})"
        
