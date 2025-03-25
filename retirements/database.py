from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database URL
DATABASE_URL = "sqlite:///./retirements.db"

# Create Engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session Local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Model
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
