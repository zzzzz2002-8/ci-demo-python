import pytest
import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 现在可以直接导入
from src.calculator import add, subtract, multiply, divide

def test_add():
    """测试加法功能"""
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(2.5, 3.5) == 6.0

def test_subtract():
    """测试减法功能"""
    assert subtract(10, 4) == 6
    assert subtract(5, 5) == 0
    assert subtract(3.5, 1.5) == 2.0

def test_multiply():
    """测试乘法功能"""
    assert multiply(2, 6) == 12
    assert multiply(0, 100) == 0
    assert multiply(4, -3) == -12

def test_divide():
    """测试除法功能"""
    assert divide(20, 5) == 4
    assert divide(10, 2.5) == 4.0
    assert divide(0, 5) == 0

def test_divide_by_zero():
    """测试除零错误"""
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "除零错误" in str(excinfo.value)