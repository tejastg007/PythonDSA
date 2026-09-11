# https://leetcode.com/problems/pascals-triangle-ii/description/

# return row of the given index
def getRow(rowIndex: int) -> list[int]:
    previousRow = [0]*(rowIndex+1)
    result = [0]*(rowIndex+1)
    for i in range(rowIndex+1):
        for j in range(i+1):
            if j == 0 or j == i:
                result[j] = 1
            else:
                result[j] = previousRow[j]+previousRow[j-1]
        if rowIndex == i:
            print(result)

        previousRow = result[:]


getRow(5)
