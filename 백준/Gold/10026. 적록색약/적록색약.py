from collections import deque
n = int(input())
grid = [[*input()] for _ in range(n)]
nor, abn = 0, 0

visited = [[0]*n for _ in range(n)]
def bfs(i, j, p, sign):
    queue = deque([[i, j]])
    while queue:
        data = queue.popleft()
        for my, mx in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            ly, lx = data[0]+my, data[1]+mx
            if n > ly >= 0 and n > lx >= 0:
                if visited[ly][lx] == 0 and grid[ly][lx] == p:
                    visited[ly][lx] = sign
                    queue.append([ly, lx])
sign = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, grid[i][j], sign)
            sign += 1
nor = sign-1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R' or grid[i][j] == 'G':
            grid[i][j] = 'C'
visited = [[0]*n for _ in range(n)]
sign = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, grid[i][j], sign)
            sign += 1
abn = sign-1
print(nor, abn)