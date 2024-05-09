from collections import deque
n, m = map(int, input().split())
city = [[*map(int, input().split())] for _ in range(m)]

def bfs(n, m, city):
    queue = deque([[0, 0]])
    visited = [[0] * n for _ in range(m)]
    while queue:
        now = queue.popleft()
        if now[0] == n-1 and now[1] == m-1 and city[now[1]][now[0]] == 1:
            return 1
        if not visited[now[1]][now[0]] and city[now[1]][now[0]] == 1:
            visited[now[1]][now[0]] = 1
            for i, j in zip([0, 1], [1, 0]):
                if now[0]+i < n and now[1]+j < m:
                    queue.append([now[0]+i, now[1]+j])
    return 0

if bfs(n, m, city):
    print('Yes')
else:
    print('No')