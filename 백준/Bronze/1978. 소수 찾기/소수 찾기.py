def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
n = int(input())
count = 0
for i in [*map(int, input().split())]:
    if i == 1:
        continue
    if isPrime(i): count += 1
print(count)