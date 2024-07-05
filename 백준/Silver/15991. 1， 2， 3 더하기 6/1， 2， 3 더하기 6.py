d = {i+1: j for i, j in zip(range(7), [1, 2, 2, 3, 3, 6, 6])}
for i in range(8, 100001):
    d[i] = d[i-2] + d[i-4] + d[i-6]

for _ in range(int(input())):
    n = int(input())
    print(d[n] % 1000000009)