def solution(s):
    flag = True
    ans = ""
    for i in s:
        if i == ' ':
            flag = True
            ans += ' '
            continue
        if flag:
            ans += i.upper()
            flag = False
        else:
            ans += i.lower()
            flag = True
    return ans