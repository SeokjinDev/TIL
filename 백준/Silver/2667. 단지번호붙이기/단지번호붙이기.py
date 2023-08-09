n = int(input())
m = [[*input()] for _ in range(n)]
def bfs(y, x):
    stack = [[y, x]]
    m[y][x] = '0'
    count = 1
    while stack:
        ny, nx = stack.pop()
        for my, mx in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            ty, tx = ny + my, nx + mx
            if n > ty >= 0 and n > tx >= 0 and m[ty][tx] == '1':
                stack.append([ty, tx])
                m[ty][tx] = '0'
                count += 1
    return count
result = []
for i in range(n):
    for j in range(n):
        if m[i][j] == '1':
            result.append(bfs(i, j))
print(len(result))
[print(r) for r in sorted(result)]