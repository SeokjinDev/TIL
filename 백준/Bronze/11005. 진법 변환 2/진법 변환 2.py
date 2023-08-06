n, b = map(int, input().split())
num = ''
while n:
    if n % b > 9:
        num += chr(n % b + 55)
    else:
        num += str(n % b)
    n = n // b
print(num[::-1])