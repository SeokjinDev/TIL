from heapq import heappop, heappush
from sys import stdin
heap = []

n = int(stdin.readline())
for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap, [abs(x), x])