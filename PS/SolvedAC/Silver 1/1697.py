# baekjoon 1697
# https://www.acmicpc.net/problem/1697
# Silver 1

from collections import deque

n, k = map(int, input().split())
length = k-n

def bfs(s, e):
    queue = deque([[s, 0]])
    visited = {}
    while(1):
        data = queue.popleft()
        num, floor = data
        if num == e:
            print(floor)
            break
        elif num < 0 or 100000 < num:
            continue
        elif visited.get(num):
            continue
        visited[num] = 1
        queue.extend([[num*2, floor+1], [num-1, floor+1], [num+1, floor+1]])

bfs(n, k)