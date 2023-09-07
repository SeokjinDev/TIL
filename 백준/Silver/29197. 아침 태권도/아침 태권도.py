from sys import stdin
check = {}
count = 0
for _ in range(int(input())):
    x, y = map(int, stdin.readline().split())
    slope = y/x
    if check.get(slope) == None:
        check[slope] = 1
        count += 1
print(count)