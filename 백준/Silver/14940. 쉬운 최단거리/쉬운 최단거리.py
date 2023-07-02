from collections import deque
n, m = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            goal = [i, j]
queue.append(goal)
visited[goal[0]][goal[1]] = 0
while queue:
    data = queue.popleft()
    for my, mx in zip([-1, 1, 0, 0, ], [0, 0, -1, 1]):
        ly, lx = data[0]+my, data[1]+mx
        if n > ly >= 0 and m > lx >= 0 and visited[ly][lx] == -1 and board[ly][lx] != 0:
            visited[ly][lx] = visited[data[0]][data[1]]+1
            queue.append([ly, lx])
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            visited[i][j] = 0

for v in visited:
    print(*v)