n = int(input())
data = [*map(int, input().split())]
s = int(input())
for i in range(n):
    m = max(data[i:min(n, i+s+1)])
    mp = data.index(m)
    for j in range(mp, i, -1):
        data[j], data[j-1] = data[j-1], data[j]
    s -= mp - i 
    if s < 1:
        break
print(*data)