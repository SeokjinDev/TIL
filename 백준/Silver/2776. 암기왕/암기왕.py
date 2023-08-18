def bs(num, n, memo):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if memo[mid] == num:
            return True
        elif memo[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    m1 = sorted([*map(int, input().split())])
    m = int(input())
    m2 = [*map(int, input().split())]
    for i in m2:
        print(1 if bs(i, n, m1) else 0)