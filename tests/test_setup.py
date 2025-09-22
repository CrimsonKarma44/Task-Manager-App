import pytest
from src.utils import setup

def test_setup_module_importable():
    assert hasattr(setup, "__file__")
