def magicSquare(inputArray):
    totalConversions = 0
    possibleValues = []
    numberOfValues = []
    for row in inputArray:
        rowTotal = 0
        for item in row:
            rowTotal += inputArray[inputArray.index(row)][row.index(item)]
        if rowTotal in possibleValues:
            numberOfValues[possibleValues.index(rowTotal)] += 1
        else:
            possibleValues.append(rowTotal)
            numberOfValues.append(1)


    return possibleValues


print(magicSquare([[1,2,3],[4,5,6],[7,8,9]]))

