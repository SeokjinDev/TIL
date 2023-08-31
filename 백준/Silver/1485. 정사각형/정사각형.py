for _ in range(int(input())):
    points = [[*map(int, input().split())] for _ in range(4)]
    lens = []
    for i in range(3):
        for j in range(i+1, 4):
            lens.append(sum([abs(points[i][k]-points[j][k])**2 for k in range(2)]))
    lens.sort()
    if len(set(lens[:4])) == 1 and len(set(lens[4:])) == 1:
        print(1)
    else:
        print(0)