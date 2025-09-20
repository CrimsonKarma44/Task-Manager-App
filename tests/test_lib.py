import pytest
from src.utils import lib

def test_lib_module_importable():
    assert hasattr(lib, "__file__")
