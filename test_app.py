import os

def test_app_exists():
    assert os.path.exists("app.py"), "Файл app.py отсутствует!"
