# factorial and fibonacci program
def fib(n):
    if n <= 1:
        return n
    ans = fib(n-1)+fib(n-2)
    return ans


def facto(n):
    if n <= 1:
        return 1
    return n * facto(n-1)


print(facto(5))
print(fib(7))  # nth term only
