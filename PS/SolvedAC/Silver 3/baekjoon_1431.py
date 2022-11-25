# baekjoon 1431
# https://www.acmicpc.net/problem/1431
# Silver 3

def check(data):
    return sum([int(i) if i.isdigit() else 0 for i in data])

# reverse order of conditions
n = int(input())
s = sorted([input() for _ in range(n)])
s = sorted(s, key=lambda x: check(x))
s = sorted(s, key=lambda x: len(x))
[print(i) for i in s]