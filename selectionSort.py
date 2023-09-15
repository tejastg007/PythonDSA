# selection sort
a = [64, 32, 24, 54, -1, 34, 34, 24, 65]
n = len(a)
for i in range(n):
    smallestIndex = i
    for j in range(i, n):
        if a[j] < a[smallestIndex]:
            smallestIndex = j
    a[i], a[smallestIndex] = a[smallestIndex], a[i]
print(a)