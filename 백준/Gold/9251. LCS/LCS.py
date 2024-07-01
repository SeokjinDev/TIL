a = input()
b = input()
la, lb = len(a), len(b)
table = [[0] * (lb+1) for _ in range(la+1)]

for i in range(1, la+1):
    for j in range(1, lb+1):
        if a[i-1] == b[j-1]:
            table[i][j] += table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i][j-1], table[i-1][j])
print(table[la][lb])