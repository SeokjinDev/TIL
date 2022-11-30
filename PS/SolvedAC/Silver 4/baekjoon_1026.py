# baekjoon 1026
# https://www.acmicpc.net/problem/1026
# Silver 4

n = int(input())
a = sorted([*map(int, input().split())])
b = sorted([*map(int, input().split())], reverse=True)
print(sum([a*b for a,b in zip(a, b)]))