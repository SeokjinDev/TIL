def hanoi(n, s, m, e):
    if n == 1:
        print(s, e)
        return
    hanoi(n-1, s, e, m)
    hanoi(1, s, m, e)
    hanoi(n-1, m, s, e)
n = int(input())
print(2**n-1)
if n <= 20:
    hanoi(n, 1, 2, 3)