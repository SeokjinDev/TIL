from heapq import heappop, heappush
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
g = {i+1: [] for i in range(v)}
for _ in range(e):
    s, e, c = map(int, input().split())
    g[s].append([c, e])

visited = {i+1: float('INF') for i in range(v)}
pq = []
heappush(pq, [0, start])
visited[start] = 0

while pq:
    cost, node = heappop(pq)
    if visited[node] < cost:
        continue
    for nc, nn in g[node]:
        distance = cost + nc
        if visited[nn] > distance:
            visited[nn] = distance
            heappush(pq, [distance, nn])

for v in visited.values(): print('INF' if v == float('inf') else v)