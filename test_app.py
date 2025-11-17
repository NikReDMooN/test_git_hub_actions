import pytest
import os

def test_app_exists():
    """Проверка наличия файла app.py"""
    assert os.path.exists("app.py"), "File app.py not found"