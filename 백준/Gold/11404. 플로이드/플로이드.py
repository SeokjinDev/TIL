from math import inf
import sys
input = sys.stdin.readline
n = int(input())
graph = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
for m in range(1, n+1):
    for s in range(1, n+1):
        for e in range(1, n+1):
            if s==e:
                continue
            if graph[s][e] > graph[s][m] + graph[m][e]:
                graph[s][e] = graph[s][m] + graph[m][e]

for r in graph[1:]:
    for c in r[1:]:
        print(0 if c == inf else c, end=' ')
    print()