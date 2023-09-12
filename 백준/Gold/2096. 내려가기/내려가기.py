n = int(input())
d1 = d2 = [*map(int, input().split())]
for i in range(n-1):
    data = [*map(int, input().split())]
    d1 = [data[0] + max(d1[:2]), data[1] + max(d1[:]), data[2] + max(d1[1:])]
    d2 = [data[0] + min(d2[:2]), data[1] + min(d2[:]), data[2] + min(d2[1:])]
print(max(d1), min(d2))