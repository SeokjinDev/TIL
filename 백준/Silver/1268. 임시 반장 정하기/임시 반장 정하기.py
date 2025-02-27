t = int(input())
b = [[*map(int, input().split())] for _ in range(t)]

friends = {i: set() for i in range(t)}

for i in range(t):
    for j in range(5):
        for k in range(i+1, t):
            if b[i][j] == b[k][j]:
                friends[i].add(k)
                friends[k].add(i)

cnt = [len(friends[i]) for i in range(t)]
print(cnt.index(max(cnt))+1)