from collections import deque
n, m = map(int, input().split())
friends = {}
for _ in range(m):
    a, b = map(int, input().split())
    if friends.get(a):
        friends[a].append([a, b])
    else:
        friends[a] = [[a, b]]
    if friends.get(b):
        friends[b].append([b, a])
    else:
        friends[b] = [[b, a]]

def bfs(start):
    visited = [0] * (n+1)
    queue = deque(friends[start])
    while queue:
        s, e = queue.popleft()
        if visited[e] == 0 and start != e:
            visited[e] = visited[s]+1
            queue.extend(friends[e])
    return sum(visited)

result = [bfs(i+1) for i in range(n)]
print(result.index(min(result))+1)