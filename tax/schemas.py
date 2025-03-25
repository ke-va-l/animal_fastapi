from pydantic import BaseModel

class QuestionBase(BaseModel):
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    answer: str

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int

    class Config:
        orm_mode = True
