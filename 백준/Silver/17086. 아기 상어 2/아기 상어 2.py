from collections import deque

n, m = map(int, input().split())
q = deque([])
g = []
for i in range(n):
    for j, ele in zip(range(m), r:=[*map(int, input().split())]):
        if ele == 1:
            q.append([i, j])
    g.append(r)
while q:
    x, y = q.popleft()
    for i, j in zip([0, 0, -1, 1, -1, -1, 1, 1],
                    [-1, 1, 0, 0, -1, 1, -1, 1]):
        if 0 <= x+i < n and 0 <= y+j < m:
            if g[x+i][y+j] == 0:
                g[x+i][y+j] = g[x][y]+1
                q.append([x+i, y+j])
mValue = 0
for i in range(n):
    for j in range(m):
        if mValue < g[i][j]:
            mValue = g[i][j]
print(mValue-1)