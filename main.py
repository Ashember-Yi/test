"""命令行计算器入口。"""

from calculate import OPERATIONS, calculate


def read_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("输入无效，请输入一个数字。")


def format_number(value):
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:.12g}" if isinstance(value, float) else str(value)


def main():
    history = []
    print("多功能计算器")
    print("操作：+  -  *  /  %  **  sqrt  !  percent  1/x  abs")
    print("其他命令：history（历史）、clear（清空历史）、help（帮助）、q（退出）")

    while True:
        operation = input("\n请输入操作：").strip().lower()
        if operation in {"q", "quit", "exit"}:
            print("再见！")
            break
        if operation == "help":
            print("+ - * / % 为基础运算；** 为幂；sqrt 为平方根；! 为阶乘；")
            print("percent 将数字转换为百分数；1/x 求倒数；abs 求绝对值。")
            continue
        if operation == "history":
            print("\n".join(history) if history else "暂无计算历史。")
            continue
        if operation == "clear":
            history.clear()
            print("历史记录已清空。")
            continue
        if operation not in OPERATIONS:
            print("未知操作，请输入 help 查看支持的操作。")
            continue

        _, operand_count = OPERATIONS[operation]
        operands = [read_number(f"请输入第 {i + 1} 个数字：") for i in range(operand_count)]
        try:
            result = calculate(operation, *operands)
            expression = f" {operation} ".join(format_number(n) for n in operands)
            if operand_count == 1:
                expression = f"{operation}({format_number(operands[0])})"
            record = f"{expression} = {format_number(result)}"
            history.append(record)
            print(f"结果：{format_number(result)}")
        except (ValueError, TypeError, OverflowError) as error:
            print(f"计算错误：{error}")


if __name__ == "__main__":
    main()
