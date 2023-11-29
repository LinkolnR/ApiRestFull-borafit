from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from sqlalchemy_utils import create_database, database_exists

load_dotenv(override=True)

host = os.getenv('DB_HOST') 
# port = os.getenv('DB_PORT')
database_name = os.getenv('DB_NAME') 
user = os.getenv('DB_USER') 
password = os.getenv('DB_PASSWORD') 

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}/{database_name}"

if not database_exists(SQLALCHEMY_DATABASE_URL):
    create_database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
