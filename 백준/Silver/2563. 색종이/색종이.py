board = [[0]*100 for _ in range(100)]
for _ in range(int(input())):
    s, e = map(int, input().split())
    for i in range(e-10, e):
        for j in range(s, s+10):
            board[i][100-j] = 1
count = 0
for i in range(100):
    count += board[i].count(1)
print(count)