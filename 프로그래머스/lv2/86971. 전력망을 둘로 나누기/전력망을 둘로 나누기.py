from collections import deque

def makeRelation(wires):
    relations = {}
    for a, b in wires:
        if relations.get(a):
            relations[a].append(b)
        else:
            relations[a] = [b]
        if relations.get(b):
            relations[b].append(a)
        else:
            relations[b] = [a]
    return relations

def bfs(s, n, relations):
    visited = [0] * (n+1)
    queue = deque([s])
    count = 0
    while queue:
        data = queue.popleft()
        if visited[data] == 0:
            visited[data] = 1
            count += 1
            if relations.get(data):
                queue.extend(relations[data])
    return count


def solution(n, wires):
    result = n
    relations = makeRelation(wires)
    for a, b in wires:
        relations[a].remove(b)
        relations[b].remove(a)
        result = min(abs(bfs(a, n, relations) - bfs(b, n, relations)), result)
        relations[a].append(b)
        relations[b].append(a)

    answer = result
    return answer