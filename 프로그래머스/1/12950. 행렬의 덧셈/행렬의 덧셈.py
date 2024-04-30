def solution(arr1, arr2):
    return [[i2+j2 for i2, j2 in zip(i1, j1)] for i1, j1 in zip(arr1, arr2)]