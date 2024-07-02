from collections import deque
from math import inf

l = 100001
n, m = map(int, input().split())

q = deque([n])
visited = [inf] * l
visited[n] = 0

while q:
    d = q.popleft()
    if d == m:
        print(visited[d])
        break
    if 0 <= d*2 < l:
        if visited[d*2] > visited[d]:
            visited[d*2] = visited[d]
            q.append(d*2)
    for i in [d-1, d+1]:
        if 0 <= i < l:
            if visited[i] > visited[d]+1:
                visited[i] = visited[d]+1
                q.append(i)