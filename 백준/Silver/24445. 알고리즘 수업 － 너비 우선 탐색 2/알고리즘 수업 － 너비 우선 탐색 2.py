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
visited = [0] * (n+1)
visited[r] = 1
c = 2
while q:
    u = q.popleft()
    for v in sorted(graph[u], reverse=True):
        if visited[v] == 0:
            visited[v] = c
            c += 1
            q.append(v)
for v in visited[1:]:
    print(v)