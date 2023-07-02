from collections import deque
nodes = {}
n, m = map(int, input().split())
for i in range(n-1):
    a, b, c = map(int, input().split())
    if a in nodes:
        nodes[a].append([b, c])
    else:
        nodes[a] = [[b, c]]
    if b in nodes:
        nodes[b].append([a, c])
    else:
        nodes[b] = [[a, c]]
find = [[*map(int, input().split())] for _ in range(m)]

def bfs(s, e):
    visited = [-1] * (n+1)
    queue = deque([s])
    visited[s] = 0
    while queue:
        node = queue.popleft()
        data = nodes[node]
        for d in data:
            if visited[d[0]] == -1:
                visited[d[0]] = d[1]+visited[node]
                queue.append(d[0])
            if d[0] == e:
                return visited[e]

for s, e in find:
    print(bfs(s, e))