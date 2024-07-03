n = int(input())
x, y = map(int, input().split())
r = 4
for i in [1, n]:
    if x == i: r -= 1
    if y == i: r -= 1
print(r)