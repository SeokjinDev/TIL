from math import lcm
from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    c = False
    while x <= lcm(m, n):
        if x%n == y%n:
            c = True
            break
        x += m
    if c:
        print(x)
    else:
        print(-1)