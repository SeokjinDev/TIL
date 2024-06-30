from math import ceil
n = int(input())
ts = [*map(int, input().split())]
t, p = map(int, input().split())
print(sum([ceil(i/t) for i in ts]))
print(n//p, (n%p))