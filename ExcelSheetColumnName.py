# https://leetcode.com/problems/excel-sheet-column-title/description/

columnNumber = 702

ans = []

while columnNumber >= 26:
    digit = (columnNumber % 26)
    if digit == 0:
        digit = 26
    char = chr(64+digit)
    ans.append(char)
    remaining = columnNumber//26
    if remaining == 1 and columnNumber % 26 == 0:
        columnNumber = 0
        break
    columnNumber = columnNumber//26
    print('digit : ', digit, 'char : ', char, " ; column : ", columnNumber)


if columnNumber < 26 and columnNumber > 0:
    if digit== 26:
        ans.append('A')
    else:
        digit = (columnNumber % 26)
        char = chr(64+digit)
        ans.append(char)

print(''.join(ans[::-1]))
