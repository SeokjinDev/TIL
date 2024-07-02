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
def dfs(r, idx):
    global visited, graph
    visited[r] = idx
    for g in sorted(graph[r], reverse=True):
        if visited[g] == -1:
            dfs(g, idx+1)
    return

dfs(r, 0)
for i in visited[1:]:
    print(i)