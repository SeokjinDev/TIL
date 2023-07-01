n = int(input())
dice = [*map(int, input().split())]
s = 0

if n == 1:
    print(sum(dice)-max(dice))
else:
    sideList = sorted([min(dice[0], dice[5]),
                       min(dice[1], dice[4]),
                       min(dice[2], dice[3])])
    s = sum(sideList) * 4
    s += sum(sideList[:2]) * (8*(n-2) + 4)
    s += sideList[0] * (5*((n-2)**2) + 4*(n-2))
    print(s)