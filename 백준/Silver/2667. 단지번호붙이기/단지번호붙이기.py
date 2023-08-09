from collections import deque

n = int(input())
square = [[*input()] for _ in range(n)]

def dfs(y, x, m):
    queue = deque([[y, x]])
    m[y][x] = '0'
    count = 1
    while queue:
        ny, nx = queue.popleft()
        for my, mx in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            ty, tx = ny + my, nx + mx
            if n > ty >= 0 and n > tx >= 0:
                if m[ty][tx] == '1':
                    queue.append([ty, tx])
                    m[ty][tx] = '0'
                    count += 1
    return m, count

result = []
for i in range(n):
    for j in range(n):
        if square[i][j] == '1':
            square, d = dfs(i, j, square)
            result.append(d)
print(len(result))
[print(r) for r in sorted(result)]