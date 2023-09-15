# insertion sort
a = [64, 32, 24, 54, -1, 34, 34, 24, 65]
n = len(a)

for i in range(1, n):
    j = i
    while j > 0 and a[j] < a[j-1]:
        a[j], a[j-1] = a[j-1], a[j]
        j -= 1

print(a)