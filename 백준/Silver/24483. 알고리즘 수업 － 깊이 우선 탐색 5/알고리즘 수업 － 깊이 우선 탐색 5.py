import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1] * (n+1)
idx = 1
def dfs(r, depth):
    global visited, graph, idx
    visited[r] = depth * idx
    idx += 1
    for g in sorted(graph[r]):
        if visited[g] == -1:
            dfs(g, depth+1)
    return

dfs(r, 0)
print(sum([v if v != -1 else 0 for v in visited]))
