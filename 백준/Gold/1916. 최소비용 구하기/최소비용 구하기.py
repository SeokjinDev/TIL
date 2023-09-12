from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
g = {i+1: [] for i in range(n)}
visited = {i+1: float('inf') for i in range(n)}
for _ in range(m):
    s, e, c = map(int, input().split())
    g[s].append([c, e])
s, e = map(int, input().split())

Pqueue = []
heappush(Pqueue, [0, s])
visited[s] = 0

while Pqueue:
    d, n = heappop(Pqueue)
    if visited[n] < d:
        continue
    for nd, nn in g[n]:
        distance = d + nd
        if visited[nn] > distance:
            visited[nn] = distance
            heappush(Pqueue, [distance, nn])
print(visited[e])