from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#autocommit: no va a haber un commit automatico
#autoflush: no limpia automaticamente el buffer
#bind: hace referencia a la creacion de la conexion

Base = declarative_base()