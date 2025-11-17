import os
import subprocess

def test_app_file_exists():
    """Тест проверяет наличие файла app.py"""
    assert os.path.exists("app.py"), "Файл app.py не найден"

def test_app_runs_correctly():
    """Тест проверяет, что приложение запускается и выводит правильную фразу"""
    result = subprocess.run(["python", "app.py"], capture_output=True, text=True)
    assert "it's my workflow" in result.stdout