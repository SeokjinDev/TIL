n = int(input())
fs = [*map(int, input().split())]
kindNum = 0
kindDict = {i+1: 0 for i in range(10)}
l, r = 0, 0
cnt = 0
result = 0

while r < n:
    if kindDict[fs[r]] == 0:
        kindNum += 1
    kindDict[fs[r]] += 1
    cnt += 1

    if kindNum > 2:
        kindDict[fs[l]] -= 1
        if kindDict[fs[l]] == 0:
            kindNum -= 1
        cnt -= 1
        l += 1  

    result = max(result, cnt)

    r += 1
print(result)