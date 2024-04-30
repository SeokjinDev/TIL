def solution(d, budget):
    d.sort()
    cost, cnt = 0, 0
    for i in d:
        cost += i
        if cost <= budget:
            cnt += 1
    return cnt