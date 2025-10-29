import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student

# Настройки подключения к БД - ЗАМЕНИТЕ НА СВОИ!
DB_URL = "postgresql://postgres:password@localhost:5432/test_database"

@pytest.fixture(scope="function")
def db_session():
    """Фикстура для создания сессии БД"""
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    # Очистка после теста
    session.query(Student).filter(Student.is_deleted == False).delete()
    session.commit()
    session.close()