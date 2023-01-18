# baekjoon 1003
# https://www.acmicpc.net/problem/1003
# Silver 3

for _ in range(int(input())):
    c0 = [1, 0]
    c1 = [0, 1]
    n = int(input())
    for i in range(n-1):
        c0 = [c0[1], c0[0]+c0[1]]
        c1 = [c1[1], c1[0]+c1[1]]
    if n < 2:
        print(c0[n], c1[n])
    else:
        print(c0[1], c1[1])