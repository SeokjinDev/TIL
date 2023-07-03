from collections import deque

n = int(input())
inputData = [*map(int, input().split())]
delIndex = int(input())

nodes = {}
for i in range(n):
    data = inputData[i]
    if i == delIndex:
        pass
    elif nodes.get(data) is None:
        nodes[data] = [i]
    else:
        nodes[data].append(i)

count = 0
if nodes.get(-1) is not None:
    queue = deque([])
    queue.append(*nodes[-1])

    while queue:
        data = queue.popleft()
        if nodes.get(data) is None:
            count += 1
        else:
            queue.extend(nodes[data])
print(count)