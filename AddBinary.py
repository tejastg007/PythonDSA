# https://leetcode.com/problems/add-binary/description/

def AddBinary(a, b):

    a = a.rjust(len(b), '0')
    b = b.rjust(len(a), '0')
    ans = ''
    carry = 0
    for i in range(len(a)-1, -1, -1):
        if a[i] == '1' and b[i] == '1':
            if carry == 1:
                ans = '1'+ans
            else:
                ans = '0'+ans
            carry = 1
        elif a[i] == '0' and b[i] == '0':
            if carry == 1:
                ans = '1'+ans
            else:
                ans = '0'+ans
            carry = 0
        else:
            if carry == 1:
                ans = '0'+ans
                carry = 1
            else:
                ans = '1'+ans
                carry = 0

    if carry == 1:
        ans = '1'+ans
    print(ans)


a = "11"
b = "1"
AddBinary(a, b)
