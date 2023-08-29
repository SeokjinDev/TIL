a, b, c = map(int, input().split())
def mul(a, n, c):
    if n == 1:
        return a % c
    pre = mul(a, n//2, c)
    if n % 2:
        return (pre * pre * a) % c
    else:
        return (pre * pre) % c
print(mul(a, b, c))