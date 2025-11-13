"""
Скрипт для запуска тестов в трех режимах
"""
import subprocess
import sys


def run_tests(test_type="all"):
    """
    Запуск тестов в указанном режиме
    
    Args:
        test_type (str): Тип тестов для запуска - "all", "ui", "api"
    """
    commands = {
        "all": ["pytest", "tests/", "-v"],
        "ui": ["pytest", "tests/test_ui.py", "-v", "-m", "ui"],
        "api": ["pytest", "tests/test_api.py", "-v", "-m", "api"]
    }
    
    if test_type not in commands:
        print("❌ Неизвестный тип тестов. Используйте: all, ui, api")
        return 1
    
    command = commands[test_type]
    print(f"🚀 Запуск {test_type} тестов: {' '.join(command)}")
    
    try:
        result = subprocess.run(command)
        if result.returncode == 0:
            print("✅ Все тесты прошли успешно!")
        else:
            print("❌ Некоторые тесты не прошли")
        return result.returncode
    except FileNotFoundError:
        print("❌ Ошибка: pytest не найден. Установите зависимости: pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    # Определяем тип тестов из аргументов командной строки
    test_type = sys.argv[1] if len(sys.argv) > 1 else "all"
    
    if test_type not in ["all", "ui", "api"]:
        print("Доступные режимы запуска:")
        print("  python run_tests.py all   - все тесты")
        print("  python run_tests.py ui    - только UI тесты") 
        print("  python run_tests.py api   - только API тесты")
        sys.exit(1)
    
    exit_code = run_tests(test_type)
    sys.exit(exit_code)