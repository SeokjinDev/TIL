def solution(n):
    t = []
    ans, idx = 0, 0
    while n:
        t.append(n % 3)
        n = n//3
    while t:
        ans += t.pop() * (3**idx)
        idx += 1
    return ans