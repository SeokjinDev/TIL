from collections import deque

n, m = map(int, input().split())
cities = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    cities[a].append(b)
    cities[b].append(a)

def bfs(cities):
    queue = deque([1])
    visited = [-1] * (n+1)
    visited[1] = 0
    while queue:
        now = queue.popleft()
        for city in cities[now]:
            if visited[city] == -1:
                visited[city] = visited[now]+1
                queue.append(city)
    return visited

q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    cities[a].append(b)
    cities[b].append(a)
    ans = bfs(cities)
    print(*ans[1:])