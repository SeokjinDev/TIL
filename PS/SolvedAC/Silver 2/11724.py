# baekjoon 11724
# https://www.acmicpc.net/problem/11724
# Silver 2

from sys import stdin

n, m = map(int, input().split())
node = [[]for _ in range(n+1)]
check = [i+1 for i in range(n)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

visited = [0] * (n+1)

def dfs(graph, start):
    stack = graph[start]
    visited[start] = 1
    check.remove(start)
    while(stack):
        data = stack.pop()
        if not visited[data]:
            stack.extend(graph[data])
            visited[data] = 1
            check.remove(data)

count = 0
while check:
    dfs(node, check[0])
    count += 1
print(count)