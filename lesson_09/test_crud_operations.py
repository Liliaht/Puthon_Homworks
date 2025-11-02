import pytest
from sqlalchemy.exc import IntegrityError
from database import Student, Course

class TestCRUDOperations:
    """Тесты для операций CRUD с базой данных"""
    
    def test_create_student(self, db_session, sample_student_data):
        """Тест создания студента (CREATE)"""
        print("\n=== Тест создания студента ===")
        
        # Создаем нового студента
        new_student = Student(**sample_student_data)
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        # Проверяем, что студент создан
        assert new_student.id is not None
        assert new_student.name == sample_student_data["name"]
        assert new_student.email == sample_student_data["email"]
        assert new_student.course == sample_student_data["course"]
        assert new_student.created_at is not None
        
        # Проверяем, что студент есть в БД
        student_from_db = db_session.query(Student).filter(
            Student.email == sample_student_data["email"]
        ).first()
        
        assert student_from_db is not None
        assert student_from_db.name == sample_student_data["name"]
        
        print(f"✅ Создан студент: {student_from_db}")

    def test_update_course(self, db_session, sample_course_data):
        """Тест обновления курса (UPDATE)"""
        print("\n=== Тест обновления курса ===")
        
        # Сначала создаем курс
        course = Course(**sample_course_data)
        db_session.add(course)
        db_session.commit()
        db_session.refresh(course)
        
        original_id = course.id
        original_name = course.name
        
        # Обновляем данные курса
        course.name = "Advanced Python"
        course.description = "Продвинутое программирование на Python"
        course.duration_hours = 96
        db_session.commit()
        db_session.refresh(course)
        
        # Проверяем обновленные данные
        assert course.id == original_id
        assert course.name == "Advanced Python"
        assert course.description == "Продвинутое программирование на Python"
        assert course.duration_hours == 96
        assert course.created_at is not None
        
        # Проверяем в БД
        updated_course = db_session.query(Course).filter(
            Course.id == original_id
        ).first()
        
        assert updated_course.name == "Advanced Python"
        assert updated_course.duration_hours == 96
        
        print(f"✅ Обновлен курс: {updated_course}")

    def test_delete_student(self, db_session, sample_student_data):
        """Тест удаления студента (DELETE)"""
        print("\n=== Тест удаления студента ===")
        
        # Создаем студента
        student = Student(**sample_student_data)
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        student_id = student.id
        
        # Проверяем, что студент создан
        created_student = db_session.query(Student).filter(Student.id == student_id).first()
        assert created_student is not None
        print(f"✅ Создан студент для удаления: {created_student}")
        
        # Удаляем студента
        db_session.delete(student)
        db_session.commit()
        
        # Проверяем, что студент удален
        deleted_student = db_session.query(Student).filter(Student.id == student_id).first()
        assert deleted_student is None
        
        print(f"✅ Студент с ID {student_id} успешно удален")

    def test_create_course(self, db_session, sample_course_data2):
        """Тест создания курса"""
        print("\n=== Тест создания курса ===")
        
        # Создаем новый курс
        new_course = Course(**sample_course_data2)
        db_session.add(new_course)
        db_session.commit()
        db_session.refresh(new_course)
        
        # Проверяем, что курс создан
        assert new_course.id is not None
        assert new_course.name == sample_course_data2["name"]
        assert new_course.description == sample_course_data2["description"]
        assert new_course.duration_hours == sample_course_data2["duration_hours"]
        assert new_course.created_at is not None
        
        print(f"✅ Создан курс: {new_course}")

    def test_unique_email_constraint(self, db_session, sample_student_data):
        """Тест ограничения уникальности email"""
        print("\n=== Тест уникальности email ===")
        
        # Создаем первого студента
        student1 = Student(**sample_student_data)
        db_session.add(student1)
        db_session.commit()
        
        # Пытаемся создать второго студента с таким же email
        student2_data = sample_student_data.copy()
        student2_data["name"] = "Другой Студент"
        
        student2 = Student(**student2_data)
        db_session.add(student2)
        
        # Должны получить ошибку уникальности
        with pytest.raises(IntegrityError):
            db_session.commit()
        
        db_session.rollback()  # Откатываем транзакцию
        
        print("✅ Проверка ограничения уникальности email прошла успешно")

    def test_course_count_operations(self, db_session, sample_course_data, sample_course_data2):
        """Тест операций подсчета курсов"""
        print("\n=== Тест операций с курсами ===")
        
        # Изначально курсов нет
        initial_count = db_session.query(Course).count()
        assert initial_count == 0
        print(f"✅ Начальное количество курсов: {initial_count}")
        
        # Создаем два курса
        course1 = Course(**sample_course_data)
        course2 = Course(**sample_course_data2)
        
        db_session.add(course1)
        db_session.add(course2)
        db_session.commit()
        
        # Проверяем количество после создания
        after_create_count = db_session.query(Course).count()
        assert after_create_count == 2
        print(f"✅ Количество курсов после создания: {after_create_count}")
        
        # Удаляем один курс
        db_session.delete(course1)
        db_session.commit()
        
        # Проверяем количество после удаления
        after_delete_count = db_session.query(Course).count()
        assert after_delete_count == 1
        print(f"✅ Количество курсов после удаления: {after_delete_count}")

def test_independent_operations(db_session):
    """Дополнительный тест, демонстрирующий независимость тестов"""
    print("\n=== Тест независимости операций ===")
    
    # Этот тест должен работать независимо от других
    count_before = db_session.query(Student).count()
    
    # Создаем временного студента
    temp_student = Student(
        name="Временный Студент",
        email="temp@example.com",
        course="Временный курс"
    )
    db_session.add(temp_student)
    db_session.commit()
    
    count_after = db_session.query(Student).count()
    assert count_after == count_before + 1
    print(f"✅ Независимость тестов подтверждена: {count_before} -> {count_after}")

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])