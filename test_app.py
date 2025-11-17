import os

def test_app_file_exists():
    """Проверяем, что в проекте есть основной файл приложения app.py"""
    assert os.path.exists("app.py"), "Файл app.py не найден!"
