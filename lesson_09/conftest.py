import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Student, Course
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="function")
def db_session():
    """Фикстура для создания сессии БД с очисткой после теста"""
    DATABASE_URL = os.getenv("DATABASE_URL")
    
    engine = create_engine(DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Создаем таблицы
    Base.metadata.create_all(bind=engine)
    
    session = TestingSessionLocal()
    
    yield session
    
    # Очистка после теста - удаляем все данные из тестовых таблиц
    try:
        session.query(Student).delete()
        session.query(Course).delete()
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Ошибка при очистке данных: {e}")
    finally:
        session.close()

@pytest.fixture
def sample_student_data():
    return {
        "name": "Иван Иванов",
        "email": "ivan.ivanov@example.com",
        "course": "Математика"
    }

@pytest.fixture
def sample_course_data():
    return {
        "name": "Python Programming",
        "description": "Изучение программирования на Python",
        "duration_hours": 72
    }

@pytest.fixture
def sample_course_data2():
    return {
        "name": "Web Development",
        "description": "Разработка веб-приложений",
        "duration_hours": 48
    }