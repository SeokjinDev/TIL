import sys
input = sys.stdin.readline
n = int(input())
points = [[*map(int, input().split())] for _ in range(n)]
x = 0
l = 0
for i in range(n-2):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    x3, y3 = points[i+2]
    c = abs(x1-x2)+abs(y1-y2)+abs(x2-x3)+abs(y2-y3)-abs(x1-x3)-abs(y1-y3)
    if c > x:
        x = c
    l += abs(x1-x2)+abs(y1-y2)
l += abs(x2-x3)+abs(y2-y3)
print(l-x)