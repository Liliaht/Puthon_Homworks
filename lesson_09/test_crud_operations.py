import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from datetime import datetime

# Настройки подключения к БД - ЗАМЕНИТЕ НА СВОИ!
DB_URL = "postgresql://postgres:password@localhost:5432/test_database"

class TestCRUDOperations:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Настройка перед каждым тестом"""
        self.engine = create_engine(DB_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        
        yield
        
        # Очистка после каждого теста
        self.session.query(Student).filter(Student.is_deleted == False).delete()
        self.session.commit()
        self.session.close()
    
    def test_create_student(self):
        """Тест на добавление студента"""
        # Arrange
        student_data = {
            "name": "Иван Иванов",
            "email": "ivan@example.com"
        }
        
        # Act
        new_student = Student(**student_data)
        self.session.add(new_student)
        self.session.commit()
        self.session.refresh(new_student)
        
        # Assert
        assert new_student.id is not None
        assert new_student.name == "Иван Иванов"
        assert new_student.email == "ivan@example.com"
        assert new_student.is_active == True
        assert new_student.is_deleted == False
        assert new_student.deleted_at is None
        
        # Проверяем, что студент действительно сохранен в БД
        saved_student = self.session.query(Student).filter_by(id=new_student.id).first()
        assert saved_student is not None
        assert saved_student.name == "Иван Иванов"
    
    def test_update_student(self):
        """Тест на изменение данных студента"""
        # Arrange - создаем студента
        student = Student(name="Петр Петров", email="petr@example.com")
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        
        original_updated_at = student.updated_at
        
        # Act - обновляем данные
        student.name = "Петр Сидоров"
        student.email = "sidorov@example.com"
        self.session.commit()
        self.session.refresh(student)
        
        # Assert
        assert student.name == "Петр Сидоров"
        assert student.email == "sidorov@example.com"
        assert student.updated_at > original_updated_at  # Проверяем, что updated_at обновился
        
        # Проверяем в БД
        updated_student = self.session.query(Student).filter_by(id=student.id).first()
        assert updated_student.name == "Петр Сидоров"
    
    def test_soft_delete_student(self):
        """Тест на мягкое удаление студента"""
        # Arrange - создаем студента
        student = Student(name="Мария Иванова", email="maria@example.com")
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        
        student_id = student.id
        
        # Act - выполняем мягкое удаление
        student.is_deleted = True
        student.deleted_at = datetime.now()
        self.session.commit()
        
        # Assert - проверяем, что студент помечен как удаленный
        deleted_student = self.session.query(Student).filter_by(id=student_id).first()
        assert deleted_student.is_deleted == True
        assert deleted_student.deleted_at is not None
        
        # Проверяем, что при обычном запросе студент не возвращается
        active_students = self.session.query(Student).filter_by(is_deleted=False).all()
        assert student not in active_students
        
        # Но при явном запросе мы можем его найти
        all_students = self.session.query(Student).all()
        assert student in all_students

    def test_hard_delete_student(self):
        """Тест на физическое удаление студента"""
        # Arrange - создаем студента
        student = Student(name="Анна Смирнова", email="anna@example.com")
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        
        student_id = student.id
        
        # Act - физически удаляем студента
        self.session.delete(student)
        self.session.commit()
        
        # Assert - проверяем, что студент удален из БД
        deleted_student = self.session.query(Student).filter_by(id=student_id).first()
        assert deleted_student is None

def test_student_creation_with_fixture(db_session):
    """Тест создания студента с использованием фикстуры"""
    # Arrange
    student_data = {
        "name": "Тест Студент",
        "email": "test@example.com"
    }
    
    # Act
    new_student = Student(**student_data)
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)
    
    # Assert
    assert new_student.id is not None
    assert new_student.name == "Тест Студент"
    
    # Проверяем, что студент доступен в БД
    saved_student = db_session.query(Student).filter_by(id=new_student.id).first()
    assert saved_student is not None