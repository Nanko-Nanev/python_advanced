# def operate(operator, a, *args):
#     result = a
#     if operator == "+":
#         for el in args:
#             result += float(el)
#     elif operator == "-":
#         for el in args:
#             result -= float(el)
#     elif operator == "*":
#         for el in args:
#             result *= float(el)
#     elif operator == "/":
#         for el in args:
#             result /= float(el)
#     return int(result)

from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), args)
