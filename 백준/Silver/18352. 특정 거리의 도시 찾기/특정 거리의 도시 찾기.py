from collections import deque
from math import inf
import sys
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

ans = {}
q = deque([x])
visited = [inf] * (n+1)
visited[x] = 0
while q:
    d = q.popleft()
    for i in graph[d]:
        if visited[i] > visited[d]+1:
            visited[i] = visited[d]+1
            q.append(i)

c = False
for i, v in zip(range(n+1), visited):
    if v == k:
        print(i)
        c = True
if c == False:
    print(-1)