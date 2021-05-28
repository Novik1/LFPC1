Vn = ['S','A','B','C','D']
Vt = ['a','b','c','d','e','f','g','e']
P = ["S->Ag", "A->AbD", "A->C", "C->e", "C->CfD", "D->e"]
word = "efefebeg"

states = {}
first = {}
last = {}
precedenceMatrix = {}
allSymbols = Vn + Vt
allSymbols.append('$')

def readInput():
    for el in P:
        symbols = []
        if el[0] not in states.keys(): states[el[0]] = []
        for symbol in el:
            if symbol != '-' and symbol != '>':
                symbols.append(symbol)
        states[symbols.pop(0)].append(symbols)


def addFirstLast(leftSide, reccurentLeftSide, pos, dict):
    for rightSide in states[reccurentLeftSide]:
        if rightSide[pos] not in dict[leftSide]:
            dict[leftSide].append(rightSide[pos])
            if rightSide[pos] in Vn:
                addFirstLast(leftSide, rightSide[pos], pos, dict)


def firstLast():
    for nonTerminal in Vn:
        first[nonTerminal] = []
        last[nonTerminal] = []
        addFirstLast(nonTerminal, nonTerminal, 0, first)
        addFirstLast(nonTerminal, nonTerminal, -1, last)


def rule1(production, count):
    precedenceMatrix[production[count]][production[count + 1]].append('=')


def rule2(production, count):
    if production[count + 1] in Vn:
        for symbol in first[production[count + 1]]:
            precedenceMatrix[production[count]][symbol].append('<')

def rule3(production, count):
    if production[count] in Vn and production[count + 1] in Vt:
        for symbol in last[production[count]]:
            precedenceMatrix[symbol][production[count + 1]].append('>')
    elif production[count] in Vn and production[count + 1] in Vn:
        for symbol in last[production[count]]:
            for symbol2 in first[production[count + 1]]:
                if symbol2 in Vt:
                    precedenceMatrix[symbol][symbol2].append('>')

def initializeMatrix(array):
    for el in array:
        precedenceMatrix[el] = {}
        for element in array:
            precedenceMatrix[el][element] = []
            if el == '$' and element != '$':
                precedenceMatrix['$'][element] = ['<']
        if el != '$':
            precedenceMatrix[el]['$'] = ['>']

def completeMatrix(dict):
    initializeMatrix(allSymbols)
    for leftSide, rightSide in dict.items():
        for production in rightSide:
            if len(production) > 1:
                count = 0
                while (count < len(production) - 1):
                    rule1(production, count)
                    rule2(production, count)
                    rule3(production, count)
                    count += 1

def printMatrix(matrix):
    print("{:<3}".format(' '), end=' ')
    for element in allSymbols:
        print("{:<3}".format(element), end=' ')
    for element, arrayElement in matrix.items():
        print("\n{:<3}".format(element), end=' ')
        for symbol in arrayElement:
            if (len(arrayElement[symbol]) == 0):
                print("{:<3}".format(' '), end=' ')
            else:
                print("{:<3}".format(arrayElement[symbol][0]), end=' ')
    print()

def replaceTerm(symbols):
    for leftSide, rightSide in states.items():
        if symbols in rightSide:
            return ["<",leftSide,">"]

def printParse(array):
    for term in array:
        print(term, end="")
    print()

def verifyInput(input, matrix):
    symbols=[]
    newInput=["$"]
    i=1
    while input[i] != "$":
        if input[i] == "<":
            i +=1
            start = i-1
            symbols=[]
            while input[i] != ">":
                if input[i] == "<":
                    for j in range(start,i):
                        newInput.append(input[j])
                    symbols=[]
                    i -=1
                    break
                if input[i] in allSymbols:
                    symbols.append(input[i])
                i += 1
            i += 1
            if len(symbols) == 1:
                if input[i] != '$':
                    if matrix[input[i-2]][input[i]][0] == "=":
                        newInput.extend(["<",input[i-2],"="])
                    elif matrix[input[i - 4]][input[i-2]][0] == "=":
                        newInput.extend(["=",input[i-4],">"])
                    else:
                        newInput.extend(replaceTerm(symbols))
                else:
                    if matrix[input[start-1]][input[start+1]][0] == "=":
                        newInput.extend(["=",input[start+1],">"])
                    else:
                        newInput.extend(replaceTerm(symbols))
            elif len(symbols) > 0:
                newInput.append("<")
                for leftSide, rightSide in states.items():
                    if symbols in rightSide:
                        newInput.append(leftSide)
                        newInput.append(">")
        else:
            newInput.append(input[i])
            i += 1
    newInput.append("$")
    printParse(newInput)
   
    if len(newInput) > 5:
        verifyInput(newInput, matrix)


def parseInput(input, matrix):
    inputList = []
    
    for i in range(0, (len(input) - 1) * 2, 2):
        input = input[:i + 1] + matrix[input[i]][input[i + 1]][0] + input[i + 1:]
   
    for symbol in input:
        inputList.append(symbol)
    verifyInput(inputList, matrix)

readInput()
firstLast()
completeMatrix(states)
printMatrix(precedenceMatrix)
parseInput("$" + word + "$", precedenceMatrix)
