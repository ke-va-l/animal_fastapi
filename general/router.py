from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from general.database import get_db
from general.schemas import QuestionCreate, QuestionResponse
from general.crud import create_question, get_questions, get_question, update_question, delete_question

router = APIRouter()

# Create a question
@router.post("/", response_model=QuestionResponse)
def add_question(question: QuestionCreate, db: Session = Depends(get_db)):
    return create_question(db, question)

# Get all questions
@router.get("/", response_model=list[QuestionResponse])
def fetch_questions(db: Session = Depends(get_db)):
    return get_questions(db)

# Get a single question by ID
@router.get("/{question_id}", response_model=QuestionResponse)
def fetch_question(question_id: int, db: Session = Depends(get_db)):
    question = get_question(db, question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

# Update a question
@router.put("/{question_id}", response_model=QuestionResponse)
def modify_question(question_id: int, question: QuestionCreate, db: Session = Depends(get_db)):
    updated_question = update_question(db, question_id, question)
    if updated_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return updated_question

# Delete a question
@router.delete("/{question_id}")
def remove_question(question_id: int, db: Session = Depends(get_db)):
    deleted_question = delete_question(db, question_id)
    if deleted_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted successfully"}
