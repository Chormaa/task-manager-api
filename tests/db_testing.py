import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

load_dotenv()


TEST_DATABASE_URL = URL.create(
    drivername='postgresql+psycopg',
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('TEST_DB_NAME')
)

test_engine = create_engine(TEST_DATABASE_URL)

SessionTest = sessionmaker(bind=test_engine)

def get_test_db():
    test_db = SessionTest()
    try:
        yield test_db
    finally:
        test_db.close()
        
        


