for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    s = sorted([*map(int, input().split())])
    b = sorted([*map(int, input().split())])

    idxS, idxB = 0, 0
    while 1:
        if s[idxS] == b[idxB]:
            idxB += 1
        elif s[idxS] > b[idxB]:
            idxB += 1
        elif s[idxS] < b[idxB]:
            idxS += 1
        if idxS == n or idxB == m:
            break
    if n-idxS > 0 and m-idxB > 0:
        print("C")
    elif n-idxS > 0:
        print("S")
    elif m-idxB > 0:
        print("B")