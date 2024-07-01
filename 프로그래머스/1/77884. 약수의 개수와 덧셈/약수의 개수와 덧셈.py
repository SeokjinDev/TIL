def solution(left, right):
    ans = 0
    for i in range(left, right+1):
        c = i ** 0.5
        if c == int(c):
            ans -= i
        else:
            ans += i
    return ans