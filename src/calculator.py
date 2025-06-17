def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b

def subtract(a: float, b: float) -> float:
    """减法运算"""
    return a - b

def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b

def divide(a: float, b: float) -> float:
    """除法运算"""
    if b == 0:
        raise ValueError("除零错误：除数不能为零")
    return a / b