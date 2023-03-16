# baekjoon 2630
# https://www.acmicpc.net/problem/2630
# Silver 2

n = int(input())
paper = [[*map(int, input().split())] for _ in range(n)]
an = {'w':0, 'b':0}

def sol(x, y, n):
    point = paper[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if point != paper[i][j]:
                n = n//2
                sol(x, y, n)
                sol(x+n, y, n)
                sol(x, y+n, n)
                sol(x+n, y+n, n)
                return
    if point:
        an['b'] += 1
    else:
        an['w'] += 1

sol(0, 0, n)
print(an['w'])
print(an['b'])