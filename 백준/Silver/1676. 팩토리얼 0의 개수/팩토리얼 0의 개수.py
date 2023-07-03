n = int(input())
fac = 1
for i in range(n):
    fac *= n-i
for i in range(len(str(fac))):
    if fac % 10:
        break
    fac = fac//10
print(i)