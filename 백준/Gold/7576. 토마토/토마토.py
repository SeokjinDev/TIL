from collections import deque

m,n = map(int, input().split())
loc = [[*map(int, input().split())] for _ in range(n)]
queue = deque([])
ylist, xlist = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0

for i in range(n):
    for j in range(m):
        if loc[i][j] == 1:
            queue.append([i, j])
while queue:
    y, x = queue.popleft()
    for i in range(4):
        yloc, xloc = ylist[i] + y, xlist[i] + x
        if 0 <= yloc < n and 0 <= xloc < m and loc[yloc][xloc] == 0:
            loc[yloc][xloc] = loc[y][x] + 1
            queue.append([yloc, xloc])
for i in loc:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result, max(i))
print(result - 1)