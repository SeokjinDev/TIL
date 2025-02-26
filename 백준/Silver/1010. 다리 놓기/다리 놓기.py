def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def combination(r, n):
    return factorial(n) / (factorial(r) * factorial(n - r))

t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    print("%d" % combination(n, m))