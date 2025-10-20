# test_app.py
import os

def test_app_py_exists():
    assert os.path.exists("app.py"), "Файл app.py не найден"