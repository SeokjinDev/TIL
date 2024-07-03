from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    for j, k in zip(range(n), input()):
        if k == 'Y':
            graph[i].append(j)

ans = []
for i in range(n):
    queue = deque([[i, 0]])
    visited = [0] * (n+1)
    visited[i] = 1
    while queue:
        now, depth = queue.popleft()
        if depth == 2:
            break
        for next in graph[now]:
            if visited[next] == 0:
                visited[next] = 1
                queue.append([next, depth+1])
    ans.append(sum(visited)-1)
print(max(ans))