def solution(a):
    l = len(a)
    cnt = 2
    left = [a[0]] * l
    right = [a[l-1]] * l
    for i in range(1, l):
        left[i] = min(left[i-1], a[i])
    for i in range(l-2, -1, -1):
        right[i] = min(right[i+1], a[i])
    for i in range(1, l-1):
        if left[i] >= a[i] >= right[i] or left[i] <= a[i] <= right[i]:
            cnt += 1
    return cnt