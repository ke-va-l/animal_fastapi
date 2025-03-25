from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from login.schemas import QuestionCreate, QuestionResponse, UserCreate, Token
from login.security import pwd_context, create_access_token
from crud import create_question, get_all_questions, delete_question
from models import User
from typing import List
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Question Endpoints
@router.post("/questions/", response_model=QuestionResponse)
def add_question(question_data: QuestionCreate, db: Session = Depends(get_db)):
    return create_question(db, question_data)

@router.get("/questions/", response_model=List[QuestionResponse])
def get_questions(db: Session = Depends(get_db)):
    return get_all_questions(db)

@router.delete("/questions/{question_id}")
def remove_question(question_id: int, db: Session = Depends(get_db)):
    question = delete_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted successfully"}
# Authentication Endpoints
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        firstname=user.firstname, lastname=user.lastname,
        email=user.email, password=hashed_password, number=user.number
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == form_data.username).first()
    if not db_user or not pwd_context.verify(form_data.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.email}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type": "bearer"}
