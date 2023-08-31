from itertools import permutations
n, m = map(int, input().split())
ns = [*map(int, input().split())]
for p in sorted(set(permutations(ns, m))):
    print(*p)