from sqlalchemy.orm import Session
from retirements.models import QuestionDB
from retirements.schemas import QuestionCreate

# Create a new question
def create_question(db: Session, question: QuestionCreate):
    new_question = QuestionDB(**question.dict())
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

# Get all questions
def get_questions(db: Session):
    return db.query(QuestionDB).all()

# Get a single question by ID
def get_question(db: Session, question_id: int):
    return db.query(QuestionDB).filter(QuestionDB.id == question_id).first()

# Update a question
def update_question(db: Session, question_id: int, question_data: QuestionCreate):
    db_question = db.query(QuestionDB).filter(QuestionDB.id == question_id).first()
    if db_question:
        for key, value in question_data.dict().items():
            setattr(db_question, key, value)
        db.commit()
        db.refresh(db_question)
    return db_question

# Delete a question
def delete_question(db: Session, question_id: int):
    db_question = db.query(QuestionDB).filter(QuestionDB.id == question_id).first()
    if db_question:
        db.delete(db_question)
        db.commit()
    return db_question
