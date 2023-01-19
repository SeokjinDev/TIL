# baekjoon 1074
# https://www.acmicpc.net/problem/1074
# Silver 1

def Z(n, r, c):
    if n == 2:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        else:
            return 3
    m = n//2
    if r < m and c < m:
        return Z(m, r, c)
    elif r < m and c >= m:
        return Z(m, r, c-m) + m**2
    elif r >= m and c < m:
        return Z(m, r-m, c) + (m**2)*2
    else:
        return Z(m, r-m, c-m) + (m**2)*3

n, r, c = map(int, input().split())
print(Z(2**n, r, c))