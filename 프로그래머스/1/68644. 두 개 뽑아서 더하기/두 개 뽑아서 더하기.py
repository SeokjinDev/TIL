from itertools import combinations

def solution(numbers):
    return sorted(list(set([sum(p) for p in combinations(numbers, 2)])))