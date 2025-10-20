import os

def test_app_py_exists():
    assert os.path.exists("app.py"), "app.py not found in project root"