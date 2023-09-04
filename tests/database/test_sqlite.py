# sqlalchemy documentation: https://docs.sqlalchemy.org/en/20/orm/quickstart.html

import sys
import os
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the root directory by going up multiple levels
levels_up = 2  # Adjust this value based on your project structure
root_dir = os.path.abspath(os.path.join(script_dir, *([".."] * levels_up)))

# Add the root directory to sys.path
sys.path.append(root_dir)

# print("Modified sys.path:", sys.path)

import unittest
from app.util.unittest.custom_test_runner import CustomTestRunner
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    password: Mapped[str] = mapped_column("password", String)
    
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<User(name={self.name}, fullname={self.fullname}, password={self.password})>"

class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"<Address(email_address={self.email_address})>"
    

class TestSQLAlchemy(unittest.TestCase):
    
        def test_create_tables(self):
            Base.metadata.create_all(engine)
            with Session(engine) as session:
                john = User(
                    name="John",
                    fullname="John Doe",
                    password="123",
                    addresses=[Address(email_address="john_doe@email.com")],
                )
                peter = User(
                    name="Peter",
                    fullname="Peter Parker",
                    password="123",
                    addresses=[
                        Address(email_address="peter_parker@email.com"),
                        Address(email_address="peterparke@email.org"),
                    ]
                )
                jack = User(name="Jack", fullname="Jack Sparrow", password="123")

                session.add_all([john, peter, jack])
                session.commit()

                # Query user for validation
                session = Session(engine)
                stmt = select(User).where(User.name.in_(["John", "Peter", "Jack"]))

                results = session.execute(stmt).scalars().all()
                self.assertEqual(len(results), 3)
                self.assertEqual(results[0].name, "John")
                self.assertEqual(results[1].name, "Peter")
                self.assertEqual(results[2].name, "Jack")


if __name__ == '__main__':
    runner = CustomTestRunner()
    runner.log_failures = True
    runner.log_exceptions = True
    unittest.main(testRunner=runner)