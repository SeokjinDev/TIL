from collections import deque
n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append([a, b, c])
    g[b].append([b, a, c])

q = deque(g[1])
visited = [-1] * (n+1)
visited[1] = 0

while q:
    a, b, c = q.popleft()
    if visited[b] == -1:
        visited[b] = visited[a]+c
        q.extend(g[b])
print(max(visited))