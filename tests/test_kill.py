import pytest
from src.utils import kill

def test_kill_module_importable():
    assert hasattr(kill, "__file__")
