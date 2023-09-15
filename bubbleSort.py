# bubbel sort
a = [64, 32, 24, 54, -1, 34, 34, 24, 65]
n = len(a)
for i in range(n-1):
    for j in range(n-1-i):
        if (a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]

print(a)