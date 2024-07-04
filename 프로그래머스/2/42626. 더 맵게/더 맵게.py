from heapq import heapify, heappop, heappush
def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while 1:
        h = heappop(scoville)
        if h < K:
            if len(scoville) == 0:
                return -1
            heappush(scoville, heappop(scoville) * 2 + h)
            cnt += 1
        else:
            return cnt