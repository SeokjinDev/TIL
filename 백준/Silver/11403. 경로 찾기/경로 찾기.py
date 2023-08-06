from sys import maxsize
n = int(input())
nodes = {}
for i in range(n):
    data = [*map(int, input().split())]
    for j in range(n):
        if data[j] == 0:
            data[j] = maxsize
    nodes[i] = data

for w in range(n):
    for s in range(n):
        for e in range(n):
            if nodes[s][e] > nodes[s][w] + nodes[w][e]:
                nodes[s][e] = 1

for i in range(n):
    for j in range(n):
        print(1 if nodes[i][j] == 1 else 0 , end=' ')
    print()