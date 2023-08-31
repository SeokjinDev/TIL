for _ in range(int(input())):
    n = int(input())
    s = [[*map(int, input().split())] for _ in range(2)]
    if n > 1:
        s[0][1] = s[1][0]+s[0][1]
        s[1][1] = s[1][1]+s[0][0]
    if n > 2:
        for i in range(2, n):
            s[0][i] = s[0][i] + max(s[1][i-1], s[1][i-2])
            s[1][i] = s[1][i] + max(s[0][i-1], s[0][i-2])
    print(max(s[0][-1], s[1][-1]))