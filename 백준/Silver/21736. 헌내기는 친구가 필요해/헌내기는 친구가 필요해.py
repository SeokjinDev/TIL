from collections import deque
n, m = map(int, input().split())
campus = [[*input()] for _ in range(n)]

def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    count = 0
    queue = deque([[i, j]])
    while queue:
        data = queue.popleft()
        for y, x in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            my, mx = data[0] + y, data[1] + x
            if n > my >= 0 and m > mx >= 0 and visited[my][mx] == 0 and campus[my][mx] != 'X':
                if campus[my][mx] == 'P':
                    count += 1
                visited[my][mx] = 1
                queue.append([my, mx])
    return count

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            r = bfs(i, j)
if r:
    print(r)
else:
    print('TT')