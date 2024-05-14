def solution(n):
    board = [[0]*(i+1) for i in range(n)]
    y, x, num = 0, 0, 1
    for _ in range((n-1)//3+1):
        if n == 1:
            board[y][x] = num
            break
        for i in range(n-1):
            board[y+i][x] = num
            num += 1
        i += 1
        for j in range(n-1):
            board[y+i][x+j] = num
            num += 1
        j += 1
        for k in range(n-1):
            board[y+i-k][x+j-k] = num
            num += 1
        y, x, n = y+2, x+1, n-3
    ans = []
    for b in board:  ans.extend(b)
    return ans