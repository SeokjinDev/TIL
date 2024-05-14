board = []
ans = [0, 0]


def solution(arr):
    global board
    global ans
    board = arr
    recursion(0, 0, len(board))
    return ans

def recursion(x, y, n):
    global board
    global ans
    start = board[x][y]
    if n == 1:
        ans[start] += 1
        return
    for i in range(n):
        for j in range(n):
            if start != board[x+i][y+j]:
                n = n//2
                recursion(x, y, n)
                recursion(x, y+n, n)
                recursion(x+n, y, n)
                recursion(x+n, y+n, n)
                return
    ans[start] += 1
    return