# baekjoon 18870
# https://www.acmicpc.net/problem/18870
# Silver 2

input()
d=[*map(int, input().split())]
s=sorted([*set(d)])
c={s[i]: i for i in range(len(s))}
[print(c[i],end=' ')for i in d]