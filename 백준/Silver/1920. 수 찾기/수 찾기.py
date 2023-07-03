from sys import stdin
n = int(input())
a = set([*map(int, stdin.readline().split())])
m = int(input())
b = [*map(int, stdin.readline().split())]
[print(1 if i in a else 0) for i in b]