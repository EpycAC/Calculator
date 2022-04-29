import math
import toml
history = []
settings = toml.load("settings.toml")
operations = ["+", "-", "/", "*"]

def flip(num):
    return 1 / num

def simplify(equation):
    a = equation.split()
    b = "".join(a)
    c = list(b)
    return c

def groupNum(equ):
    equation = simplify(equ)
    equationSimplified = []
    term = []
    for i in range(len(equation)):
        if equation[i] not in operations:
            term.append(equation[i])
        elif equation[i] in operations:
            num = float("".join(term))
            equationSimplified.extend([num, equation[i]])
            term.clear()
        else:
            return("Error: invalid character")
        if i == len(equation) - 1:
            num = float("".join(term))
            equationSimplified.append(num)
    history.append(equationSimplified)
    print(equationSimplified)
    return equationSimplified

def solve(equation):
    " ".join(equation)
    print(equation)
    equation.split()
    print(equation)
    terms = equation.append("X")
    print(terms)
    moperator = []
    aoperator = []
    for i in range(len(terms)):
        if (terms[i] == "*") or (terms[i] == "/"):
            moperator.append([i, terms[i]])
        elif (terms[i] == "+") or (terms[i] == "-"):
            aoperator.append([i, terms[i]])
    print(moperator)
    print(aoperator)
    indexn = 0
    while len(moperator) > 0:
        operator = moperator[0]
        oindex = operator[0] - indexn
        if operator[1] == "*":
            newvalue = terms[oindex - 1] * terms[oindex + 1]
            print(newvalue)
        else:
            newvalue = terms[oindex - 1] / terms[oindex + 1]
            print(newvalue)
        terms = terms[:(oindex - 1)] + [newvalue] + terms[oindex + 2:]
        print(terms)

        moperator.remove(operator)
    return 0

equation = groupNum(input("Enter what you want to solve: "))
'''
if equation.lower() == "history" or "h":
    adjustedHistory = history.reverse()
    for i in range(min(len(history), 10)):
        if i <= len(history):
            prev = adjustedHistory[i]
            "".join(prev)
            print(prev)
else:
'''
print(solve(equation))
