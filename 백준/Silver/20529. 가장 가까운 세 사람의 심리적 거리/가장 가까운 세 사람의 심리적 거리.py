from itertools import combinations
def checkString(a, b):
    cnt = sum([0 if i==j else 1 for i, j in zip(a, b)])
    return cnt
for _ in range(int(input())):
    n = int(input())
    students = [*input().split()]
    if n > 32:
        print(0)
    else:
        distance = [[0] * n for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                cnt = checkString(students[i], students[j])
                distance[i][j] = cnt
                distance[j][i] = cnt
        l = [*range(n)]
        ans = 8
        for a, b, c in combinations(l, 3):
            dis = distance[a][b] + distance[b][c] + distance[a][c]
            ans = min(dis, ans)
        print(ans)