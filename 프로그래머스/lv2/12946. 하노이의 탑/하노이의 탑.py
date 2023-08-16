ans = []
def solution(n):
    hanoi(n, 1, 2, 3)
    answer = ans
    return answer
def hanoi(n, s, m, e):
    if n == 1:
        ans.append([s, e])
        return 
    hanoi(n-1, s, e, m)
    ans.append([s, e])
    hanoi(n-1, m, s, e)