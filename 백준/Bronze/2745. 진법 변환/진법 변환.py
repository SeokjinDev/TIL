n, b = input().split()
n = reversed([*n])
num = 0
for i, x in enumerate(n):
    if x.isalpha():
        x = ord(x) - 55
    else:
        x = int(x)
    num = x * (int(b) ** i) + num
print(num)