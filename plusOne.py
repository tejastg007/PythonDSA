# https://leetcode.com/problems/plus-one/description/
digits = [9, 9]

'''
# ! solution 1
number = 0
for i in range(len(digits)):
    number = (number*10)+digits[i]

number = number+1
print(number)
result = []
while number > 0:
    remainder = number % 10
    result.append(remainder)
    number = number//10

result = result[::-1]
print(result)
'''


# ! solution 2
for i in range(len(digits)-1, -1, -1):
    if digits[i]+1 != 10:
        digits[i] = digits[i]+1
        exit()

    digits[i] = 0

    if i == 0:
        digits = [1]+(digits)
        print(digits)
