"""
    Evaluate Reverse Polish Notation
    ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

from operator import add, mul, sub, floordiv

OPERATORS = {
    "+": add,
    "*": mul,
    "/": floordiv,
    "-": sub,
}


def evaluate(data):
    stack = []
    for token in data:
        if token not in OPERATORS.keys():
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            r = OPERATORS[token](num1, num2)
            stack.append(r)
    return stack.pop()


def main():
    income_list1 = ["2", "1", "+", "3", "*"]
    income_list2 = ["4", "13", "5", "/", "+"]

    answer = evaluate(income_list1)
    print("result1:", answer)
    assert answer == 9

    answer = evaluate(income_list2)
    print("result2:", answer)
    assert answer == 6


if __name__ == '__main__':
    main()
