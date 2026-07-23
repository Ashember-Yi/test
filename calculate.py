"""计算器核心功能模块。"""

import math
from numbers import Real


def _ensure_number(value, name="参数"):
    """确保参数是实数（布尔值除外）。"""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name}必须是数字")


def add(a, b):
    _ensure_number(a, "第一个参数")
    _ensure_number(b, "第二个参数")
    return a + b


def subtract(a, b):
    _ensure_number(a, "第一个参数")
    _ensure_number(b, "第二个参数")
    return a - b


def multiply(a, b):
    _ensure_number(a, "第一个参数")
    _ensure_number(b, "第二个参数")
    return a * b


def divide(a, b):
    _ensure_number(a, "被除数")
    _ensure_number(b, "除数")
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def modulo(a, b):
    _ensure_number(a, "被除数")
    _ensure_number(b, "除数")
    if b == 0:
        raise ValueError("除数不能为零")
    return a % b


def power(base, exponent):
    _ensure_number(base, "底数")
    _ensure_number(exponent, "指数")
    result = base**exponent
    if isinstance(result, complex):
        raise ValueError("结果不是实数")
    return result


def square_root(number):
    _ensure_number(number)
    if number < 0:
        raise ValueError("不能计算负数的平方根")
    return math.sqrt(number)


def factorial(number):
    _ensure_number(number)
    if number < 0 or int(number) != number:
        raise ValueError("阶乘只支持非负整数")
    return math.factorial(int(number))


def percentage(number):
    _ensure_number(number)
    return number / 100


def reciprocal(number):
    _ensure_number(number)
    if number == 0:
        raise ValueError("零没有倒数")
    return 1 / number


OPERATIONS = {
    "+": (add, 2),
    "-": (subtract, 2),
    "*": (multiply, 2),
    "/": (divide, 2),
    "%": (modulo, 2),
    "**": (power, 2),
    "sqrt": (square_root, 1),
    "!": (factorial, 1),
    "percent": (percentage, 1),
    "1/x": (reciprocal, 1),
    "abs": (abs, 1),
}


def calculate(operation, *operands):
    """按操作符执行计算，作为界面与核心逻辑的统一入口。"""
    if operation not in OPERATIONS:
        raise ValueError(f"不支持的操作：{operation}")
    function, operand_count = OPERATIONS[operation]
    if len(operands) != operand_count:
        raise ValueError(f"操作 {operation} 需要 {operand_count} 个数字")
    for index, value in enumerate(operands, start=1):
        _ensure_number(value, f"第 {index} 个参数")
    return function(*operands)
