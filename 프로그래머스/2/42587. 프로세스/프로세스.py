from collections import deque
import heapq
def solution(priorities, location):
    queue = deque([[p, i] for p, i in zip(priorities, range(len(priorities)))])
    heap = [-p for p in priorities]
    heapq.heapify(heap)
    cnt = 1
    while heap:
        h = heapq.heappop(heap)
        while queue:
            data = queue.popleft()
            if -h == data[0]:
                break
            else:
                queue.append(data)
        if data[1] == location:
            return cnt
        else:
            cnt += 1