n = int(input())
li = [[*map(int, input().split())] for _ in range(n)]
for i in range(n-1, 0, -1):
    for j in range(i):
        li[i-1][j] = li[i-1][j] + max(li[i][j], li[i][j+1])
print(li[0][0])