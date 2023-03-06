# baekjoon 9375
# https://www.acmicpc.net/problem/9375
# Silver 3

t = int(input())
for _ in range(t):
    clothes = {}
    n = int(input())
    for _ in range(n):
        name, category = input().split()
        if category in clothes:
            clothes[category].append(name)
        else:
            clothes[category] = [name]
    result = 1
    for i in clothes.values():
        result *= len(i)+1
    print(result-1)