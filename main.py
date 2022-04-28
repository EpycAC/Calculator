import math
history = []
operations = ["+", "-", "/", "*"]

def flip(num):
    return 1 / num

def simplify(equation):
    a = equation.split()
    b = "".join(a)
    c = list(b)
    return c

def groupNum(equation):
    operators = 0
    for i in range(len(equation)):
        if equation[i] in operations:
            operators += 1
    equationSimplified = []
    term = []
    for i in range(len(equation) - 1):
        if equation[i] not in operations:
            term.append(equation[index])
            print(term)
        num = float("".join(term))
        print(num)
        equationSimplified.append(num)
    return equationSimplified
equation = input("Enter what you want to solve: ")
equation = simplify(equation)
print(groupNum(equation))
