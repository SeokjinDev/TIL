from collections import defaultdict
n = int(input())
d = defaultdict(int)
d[1], d[2] = 1, 1

def fibo(num):
    if num < 3 or d[num] > 0:
        return d[num]
    else:
        mid = num // 2
        if num % 2:
            exp1, exp2 = fibo(mid), fibo(mid+1)
            d[num] = (exp1**2 + exp2**2) % 1000000007
            return d[num]
        else:
            exp0, exp1 = fibo(mid-1), fibo(mid)
            d[num] = ((2*exp0+exp1)*exp1) % 1000000007
            return d[num]

print(fibo(n))