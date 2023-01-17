# baekjoon 1406
# https://www.acmicpc.net/problem/1406
# Silver 2

from sys import stdin

i=stdin.readline
s1 = [*(i().rstrip())]
s2 = []
for _ in range(int(i())):
    c = [*i().split()]
    if c[0] == 'L' and s1:
        s2.append(s1.pop())
    elif c[0] == 'D' and s2:
        s1.append(s2.pop())
    elif c[0] == 'B' and s1:
        s1.pop()
    elif c[0] == 'P':
        s1.append(c[1])
s1.extend(reversed(s2))
print(''.join(s1))