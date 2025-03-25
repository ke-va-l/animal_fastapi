from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routes import router as main_router  # Rename to avoid conflict
from Psychology.router import router as Psychology_questions_router
from Estate.router import router as Estate_questions_router  # Ensure correct 
from retirements.router import router as retirements_ruestion_router
from Estate.database import engine,Base
from Psychology.database import engine,Base
from retirements.database import Base,engine
from tax.database import Base,engine
from tax.router import router as tax_question_router
from investment.router import router as investment_question_router
from investment.database import Base,engine
from riskmanagements.router import router as riskmanage_question_router
from riskmanagements.database import Base,engine
from general.router import router as general_question_router
from general.database import Base,engine
from professional.router import router as profesional_question_router
from professional.database import Base,engine

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include routes
app.include_router(main_router,prefix="/Questions_all", tags=["Question_all"])  # Main router
app.include_router(Psychology_questions_router, prefix="/Psychology", tags=["Psychology"])  # Psychology Questions API
app.include_router(Estate_questions_router, prefix="/Estate", tags=["Estate"])
app.include_router(retirements_ruestion_router,prefix="/Retirements", tags=["Retirements"])
app.include_router(tax_question_router,prefix="/tax", tags=["tax"])
app.include_router(investment_question_router,prefix="/investments", tags=["investments"])
app.include_router(riskmanage_question_router,prefix="/riskmanage", tags=["riskmanage"])
app.include_router(general_question_router,prefix="/general", tags=["general"])
app.include_router(profesional_question_router,prefix="/professional", tags=["professional"])


