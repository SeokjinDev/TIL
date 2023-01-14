# baekjoon 2167
# https://www.acmicpc.net/problem/2167
# Silver 5

import sys
n, m = map(int, sys.stdin.readline().split())
data = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
for _ in range(int(input())):
    i, j, x, y = map(int, sys.stdin.readline().split())
    s = 0
    for xPos in range(i-1, x):
        s += sum(data[xPos][j-1:y])
    print(s)