"""
Notes about the program:
    - Please note that this program code was made to work on python 3.10. Using it on previous versons of python or python 2 might cause numerous errors.
    - It also needs to have the toml module installed on pip. Tou can install this by typing "pip install toml" into the terminal.
    - This program is devided up into 3 files. main.py, settings.toml, and history,json. Not operating this without having these 3 files will cause errors.
    - Make sure that you only type float numbers or operations into the inpur. typing any other characters except for "history" or "h" will cause errors.
"""

import math
import toml
import json
settings = toml.load("settings.toml")
operations = ["+", "-", "/", "*"]


def simplify(equation):
    a = equation.split()
    b = "".join(a)
    c = list(b)
    return c

#Adds an item to the history.toml file
def updateHistory(item):
    history = open("history.json", "r")
    try:
        history = json.load(history)
    except:
        history = {
        "history": []
        }
    hFile = open("history.json", "w")
    hisTemp = [item] + history["history"]
    history["history"] = hisTemp
    hFile.write(json.dumps(history, indent=4))

#groups all seperated numbers together while seperating operators in the list.
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
    updateHistory(equationSimplified)
    return equationSimplified

#simplifies and solves the equation
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
    num = float(terms[0])
    return num

#The main loop
while True:
    equation = input("Enter what you want to solve: ")
    if (equation.lower() == "history") or (equation.lower() == "h"):
        print("")
        history = open("history.json", "r")
        try:
            history = json.load(history)
        except:
            history = {
            "history": []
            }
        history = history["history"]
        for i in range(min(len(history), settings["History"]["length"])):
            prev = history[i]
            temp = []
            for i in range(len(prev)):
                temp.append(str(prev[i]))
            temp = "".join(temp)
            print(temp)
            print(solve(prev))
            print("")
    else:
        equation = groupNum(equation)
        print(solve(equation))
