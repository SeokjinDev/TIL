# baekjoon 11279
# https://www.acmicpc.net/problem/11279
# Silver 2

from heapq import*
import sys
h=[]
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    if n:
        heappush(h,-n)
    else:
        print(h and -heappop(h) or 0)