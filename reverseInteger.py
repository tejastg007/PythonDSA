# https://leetcode.com/problems/reverse-integer/
def reverse(x):
    flag = -1 if x < 0 else 1
    x = x*flag
    res = 0
    while x > 0:
        res = res*10 + (x % 10)
        x = x // 10
    return res*flag


print(reverse(-123))
print(reverse(123))
