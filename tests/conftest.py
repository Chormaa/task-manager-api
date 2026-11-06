from models import Base
from database import get_db
from tests.db_testing import test_engine, get_test_db
from main import app

Base.metadata.create_all(bind=test_engine)

app.dependency_overrides[get_db] = get_test_db