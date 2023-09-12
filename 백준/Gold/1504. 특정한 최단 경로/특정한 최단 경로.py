from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
g = {i+1: [] for i in range(n)}
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append([c, b])
    g[b].append([c, a])
u, v = map(int, input().split())

def dijkstra(start, n):
    visited = {i+1: float('inf') for i in range(n)}
    pq = []
    heappush(pq, [0, start])
    visited[start] = 0
    while pq:
        cost, node = heappop(pq)
        if visited[node] < cost:
            continue
        for c, n in g[node]:
            dis = c + cost
            if visited[n] > dis:
                visited[n] = dis
                heappush(pq, [dis, n])
    return visited
dis1 = dijkstra(1, n)
dis2 = dijkstra(u, n)
dis3 = dijkstra(v, n)
path1 = dis1[u] + dis2[v] + dis3[n]
path2 = dis1[v] + dis3[u] + dis2[n]
ans = min(path1, path2)
print(ans if ans < float('inf') else -1)