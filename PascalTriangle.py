# https://leetcode.com/problems/pascals-triangle/description/
def generate(numRows: int):
    result = []
    for i in range(numRows):
        print('i', i)
        tempResult = []
        for j in range(i+1):
            print(' j', j)
            if j == 0 or j == i:
                tempResult.append(1)
            else:
                tempResult.append(result[i-1][j-1]+result[i-1][j])
        result.append(tempResult)
        print('result', result)

    print(result)


generate(5)
