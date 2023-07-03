m, n = map(int, input().split())
def checker(x):
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            return False
    return True
if m == 1: m = 2
for i in range(m, n+1):
    if checker(i):
        print(i)