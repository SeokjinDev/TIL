for _ in range(int(input())):
    x, y = map(int, input().split())
    dis = y-x
    cnt, mov, plus = 0, 1, 0
    while plus < dis:
        cnt += 1
        plus += mov
        if cnt % 2 == 0: mov += 1
    print(cnt)