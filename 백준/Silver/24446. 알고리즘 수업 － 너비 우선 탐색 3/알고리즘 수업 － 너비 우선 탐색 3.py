from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([r])
visited = [-1] * (n+1)
visited[r] = 0
while q:
    u = q.popleft()
    for v in sorted(graph[u], reverse=True):
        if visited[v] == -1:
            visited[v] = visited[u]+1
            q.append(v)
for v in visited[1:]:
    print(v)