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

def groupNum(equation):
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
    return equationSimplified

def solve(equation):
    pass

equation = input("Enter what you want to solve: ")
if equation.lower() == "history" or "h":
    adjustedHistory = history.reverse()
    for i in range(min(len(history), 10)):
        if i <= len(history):
            prev = adjustedHistory[i]
            "".join(prev)
            print(prev)
else:
    equation = simplify(equation)
    print(groupNum(equation))
