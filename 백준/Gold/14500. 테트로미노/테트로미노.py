n, m = map(int, input().split())
paper = [[*map(int, input().split())] for _ in range(n)]
mov = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[0]*m for _ in range(n)]
res = 0
def dfs(i, j, cnt, total):
    global res
    if cnt == 3:
        res = max(res, total)
        return
    for my, mx in mov:
        ny, nx = my+i, mx+j
        if n>ny>=0 and m>nx>=0 and visited[ny][nx] == 0:
            if cnt == 1:
                visited[ny][nx] = 1
                dfs(i, j, cnt+1, total+paper[ny][nx])
                visited[ny][nx] = 0    
            visited[ny][nx] = 1
            dfs(ny, nx, cnt+1, total+paper[ny][nx])
            visited[ny][nx] = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 0, paper[i][j])
        visited[i][j] = 0
print(res)