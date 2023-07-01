l = []
for _ in range(9):
    l.extend([*map(int, input().split())])
print(m:=max(l))
i = l.index(m)
print((i//9)+1, (i%9)+1)