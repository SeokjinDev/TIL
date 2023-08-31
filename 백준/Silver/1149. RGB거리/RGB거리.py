n = int(input())
h = [[*map(int, input().split())] for _ in range(n)]
for i in range(1, n):
    for a, b, c in [0, 1, 2], [1, 0, 2], [2, 0, 1]:
        h[i][a] = h[i][a] + min(h[i-1][b], h[i-1][c])
print(min(h[-1]))