from collections import deque
from math import inf
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
q = deque([s])
visited = [inf] * (n+1)
visited[s] = 0
while q:
    d = q.popleft()
    if d == e:
        print(visited[d])
        break
    for i in [-1, 1]:
        if 0 < d+i <= n and visited[d+i] > visited[d]+1:
            visited[d+i] = visited[d]+1
            q.append(d+i)
    if graph[d]:
        for g in graph[d]:
            if visited[g] > visited[d]+1:
                visited[g] = visited[d]+1
                q.append(g)