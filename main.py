def magicSquare(inputArray):
    minCost = 0
    possibleSolutions = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    indexOfSolutions = 0
    for magicSquare in possibleSolutions:
        index1 = 0
        index2 = 0
        currentCost = 0
        for section in magicSquare:
            for number in section:
                if inputArray[index1][index2] != number:

                    currentCost += abs(inputArray[index1][index2]-number)
                
                index2 += 1

            index1 += 1
            index2 = 0

        if indexOfSolutions == 0:
            minCost = currentCost
        else:    
            minCost = min(minCost, currentCost)

                
        indexOfSolutions += 1

    

    


    return minCost


print(magicSquare([[4,8,2],[4,5,7],[6,1,6]]))

