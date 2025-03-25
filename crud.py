from sqlalchemy.orm import Session
from models import Question
from login.schemas import QuestionCreate

def create_question(db: Session, question_data: QuestionCreate):
    question = Question(
        text=question_data.text,
        option_a=question_data.option_a,
        option_b=question_data.option_b,
        option_c=question_data.option_c,
        option_d=question_data.option_d,
        answer=question_data.answer,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def get_all_questions(db: Session):
    return db.query(Question).all()

def delete_question(db: Session, question_id: int):
    question = db.query(Question).filter(Question.id == question_id).first()
    if question:
        db.delete(question)
        db.commit()
    return question
