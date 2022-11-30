# baekjoon 1018
# https://www.acmicpc.net/problem/1018
# Silver 4

sb, sw = "BW"*4, "WB"*4 # start B, start W
r = 64 # result
n, m = map(int, input().split())
board = [input() for _ in range(n)]
for yMax in range(n-7): # 0 ~ y max
    for xMax in range(m-7): # 0 ~ x max
        bw, wb = 0, 0 # check two ways
        for y in range(yMax, yMax+8):
            if y % 2 == 0:
                wb += sum([1 if a!=b else 0 for a,b in zip(sw, board[y][xMax:xMax+8])])
                bw += sum([1 if a!=b else 0 for a,b in zip(sb, board[y][xMax:xMax+8])])
            else:
                wb += sum([1 if a!=b else 0 for a,b in zip(sb, board[y][xMax:xMax+8])])
                bw += sum([1 if a!=b else 0 for a,b in zip(sw, board[y][xMax:xMax+8])])
        r=min(r,wb,bw)
print(r)