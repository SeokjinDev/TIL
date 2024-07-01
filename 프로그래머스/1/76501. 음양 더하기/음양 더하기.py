def solution(absolutes, signs):
    ans = 0
    for i, j in zip(absolutes, signs):
        ans += i if j else -i
    return ans