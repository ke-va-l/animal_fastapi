from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    number = Column(String, unique=True, index=True)



class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    answer = Column(String, nullable=False)  # Correct answer
