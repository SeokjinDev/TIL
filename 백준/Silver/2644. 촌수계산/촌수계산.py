from collections import deque

n = int(input())
a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)
visited = [0] * (n+1)
queue = deque([a])
while queue:
    now = queue.popleft()
    for g in graph[now]:
        if not visited[g]:
            visited[g] = visited[now]+1
            queue.append(g)
print(visited[b] if visited[b] else -1)