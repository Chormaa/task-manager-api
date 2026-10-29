
""" Database connection configuration for the Task Manager API. """

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker


# Load environment variables from the .env file. Keeps database credentials separate from the source code
load_dotenv()

# Build the database connection URL using environment variables.
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg", #The driver psycopg acts as a bridge between SQLAlchemy and PostgreSQL
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

# Create the SQLAlchemy engine, engine manages the connections SQLAlchemy uses to communicate with PostgreSQL database.
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

