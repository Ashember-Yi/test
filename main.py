"""入口文件"""

from calculator import add, subtract, multiply, divide


def main():
    print("简单计算器")
    print(f"3 + 5 = {add(3, 5)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"8 / 2 = {divide(8, 2)}")


if __name__ == "__main__":
    main()