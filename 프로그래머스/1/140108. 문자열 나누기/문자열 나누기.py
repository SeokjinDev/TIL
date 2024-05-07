def solution(s):
    idx, res = 0, 0
    i = 0
    while idx < len(s):
        h = s[idx]
        cnt1, cnt2 = 0, 0
        for i in range(idx, len(s)):
            if h == s[i]:
                cnt1 += 1
            else:
                cnt2 += 1
            if cnt1 == cnt2:
                idx = i+1
                res += 1
                break
        if i == len(s)-1:
            if cnt1 != cnt2:
                res += 1
            break
    return res