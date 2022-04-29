import math
import toml
history = []
settings = toml.load("settings.toml")
operations = ["+", "-", "/", "*"]
print(settings)

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
    return equationSimplified

def solve(equation):
    terms = equation
    terms.append("X")
    moperator = []
    aoperator = []
    for i in range(len(terms)):
        if (terms[i] == "*") or (terms[i] == "/"):
            moperator.append([i, terms[i]])
    indexn = 0
    while len(moperator) > 0:
        operator = moperator[0]
        oindex = operator[0] - indexn
        if operator[1] == "*":
            newvalue = terms[oindex - 1] * terms[oindex + 1]
        else:
            newvalue = terms[oindex - 1] / terms[oindex + 1]
        terms = terms[:(oindex - 1)] + [newvalue] + terms[oindex + 2:]
        indexn = indexn + 2
        moperator.remove(operator)
    for i in range(len(terms)):
        if (terms[i] == "+") or (terms[i] == "-"):
            aoperator.append([i, terms[i]])
    indexn = 0
    while len(aoperator) > 0:
        operator = aoperator[0]
        oindex = operator[0] - indexn
        if operator[1] == "+":
            newvalue = terms[oindex - 1] + terms[oindex + 1]
        else:
            newvalue = terms[oindex - 1] - terms[oindex + 1]
        terms = terms[:(oindex - 1)] + [newvalue] + terms[oindex + 2:]
        indexn = indexn + 2
        aoperator.remove(operator)
    terms.remove("X")
    num = float(terms[0])
    return(num)



'''
if equation.lower() == "history" or "h":
    adjustedHistory = history.reverse()
    for i in range(min(len(history), settings["History"]["length"])):
        if i <= len(history):
            prev = adjustedHistory[i]
            "".join(prev)
            print(prev)
else:
'''
while True:
    equation = groupNum(input("Enter what you want to solve: "))
    print(solve(equation))
