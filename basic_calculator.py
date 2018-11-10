"""
    Basic calculator
"""

import re
from operator import add, sub, mul, truediv, pow

OPERATORS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
    "^": pow,
}


def tokenize(expr):
    tokens = re.findall("(?:\-?\d+(?:\.\d+)?)|(?:[+\-()*/^])", expr)
    return tokens


def simplify(tokens):
    depth = 0
    start = -1
    end = -1

    for index, token in enumerate(tokens):
        if token == "(":
            depth += 1
            if depth == 1:
                start = index
        elif token == ")":
            depth -= 1
            if depth == 0:
                end = index
                break

    if start != -1 and end != -1:
        temp = list(tokens[start + 1:end])
        inner_list = []
        tokens[start:end + 1] = [inner_list]
        inner_list.extend(temp)
        simplify(inner_list)
        simplify(tokens)


def calc(tokens):
    stack = []
    while tokens:
        token = tokens.pop(0)
        if isinstance(token, list):
            value = calc(token)
            tokens.insert(0, value)
        elif token in OPERATORS:
            stack.append(token)
        else:
            stack.append(token)

    while len(stack) != 1:
        if "^" in stack:
            index = stack.index("^") - 1
        elif "/" in stack:
            index = stack.index("/") - 1
        elif "*" in stack:
            index = stack.index("*") - 1
        else:
            index = 0
        left, op, right = stack.pop(index), stack.pop(index), stack.pop(index)
        stack.insert(index, OPERATORS[op](float(left), float(right)))

    return stack.pop()


def evaluate(expr):
    tokens = tokenize(expr)
    simplify(tokens)
    res = calc(tokens)
    return res


def main():
    input_string1 = "6 / (3 * 2) / 2 - 0.5"
    result1 = evaluate(input_string1)
    assert result1 == 0

    input_string2 = "((30 / 5) + 2) / 2 ^ 2 - 3"
    result2 = evaluate(input_string2)
    assert result2 == -1.0

    input_string3 = "(2 + -1 + 2) / -0.2"
    result3 = evaluate(input_string3)
    assert result3 == -15.0


if __name__ == '__main__':
    main()

