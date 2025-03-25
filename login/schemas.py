from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    number: str

class UserLogin(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


from pydantic import BaseModel

class QuestionCreate(BaseModel):
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    answer: str  # Correct option

class QuestionResponse(BaseModel):
    id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    answer: str

    class Config:
        from_attributes = True
