# baekjoon 1927
# https://www.acmicpc.net/problem/1927
# Silver 2

import heapq as h
import sys

heap = []
for _ in range(int(input())):
    command = int(sys.stdin.readline())
    if command:
        h.heappush(heap, command)
    else:
        if heap:
            print(h.heappop(heap))
        else:
            print(0)