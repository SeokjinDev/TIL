def solution(s):
    cnt, zeros = 0, 0
    while '1' != s:
        stL = len(s)
        s = s.replace('0', '')
        nwL = len(s)
        s = str(bin(nwL))[2:]
        zeros += stL - nwL
        cnt += 1
    return [cnt, zeros]