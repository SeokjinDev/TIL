from collections import deque

for _ in range(int(input())):
    count = 0
    n, m = map(int, input().split())
    docs = [*map(int, input().split())]
    queue = deque([[o, i] for i, o in enumerate(docs)])
    docs.sort()

    while 1:
        now = queue.popleft()
        if now[0] == docs[-1]:
            docs.pop()
            count += 1
            if now[1] == m:
                break
        else:
            queue.append(now)
    print(count)