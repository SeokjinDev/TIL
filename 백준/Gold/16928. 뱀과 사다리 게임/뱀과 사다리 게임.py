from collections import deque
n, m = map(int, input().split())
ladder, snake = {}, {}
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b
visited = [0] * 101
queue = deque([1])
while queue:
    data = queue.popleft()
    if data == 100:
        break
    for i in range(1, 7):
        nex = data+i
        if nex <= 100 and visited[nex] == 0:
            if ladder.get(nex):
                nex = ladder[nex]
            elif snake.get(nex):
                nex = snake[nex]
            if visited[nex] == 0:
                visited[nex] = visited[data]+1
                queue.append(nex)
print(visited[100])