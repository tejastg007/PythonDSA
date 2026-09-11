# https://leetcode.com/problems/add-digits/description/
num = 0
sum = num

while sum >= 10:
    sum = 0
    while num != 0:
        remainder = num % 10
        sum = sum+remainder
        num = num//10

    num = sum

print(sum)
