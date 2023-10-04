def find(s):
    codes = {2: 4, 3: 4, 4: 7, 5: 10, 6: 13, 7: 16, 8: 20, 9: 23}
    ans = ""
    for char in s:
        if char == ' ':
            print('s[ace]')
            ans += '0'
            continue
        charCode = ord(char)-64
        if charCode >= 23:
            times = charCode % codes.get(9) + 1
            button = 9
        elif charCode >= 20:
            times = charCode % codes.get(8) + 1
            button = 8
        elif charCode >= 16:
            times = charCode % codes.get(7) + 1
            button = 7
        elif charCode >= 13:
            times = charCode % codes.get(6) + 1
            button = 6
        elif charCode >= 10:
            times = charCode % codes.get(5) + 1
            button = 5
        elif charCode >= 7:
            times = charCode % codes.get(4) + 1
            button = 4
        elif charCode >= 4:
            times = charCode % codes.get(3) + 1
            button = 3
        elif charCode >= 1:
            times = charCode % codes.get(2)
            button = 2
        for i in range(times):
            ans += str(button)
        print(ans)


# 666333222993
# 666333222993
s = 'OFCXD'
find(s)
