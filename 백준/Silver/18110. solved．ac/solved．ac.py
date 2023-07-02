from sys import stdin
def r(n): return int(n)+1 if n % 1 >= .5 else int(n)
n = int(input())
opinions = sorted([int(stdin.readline()) for _ in range(n)])
if n:
    cut = r(n*0.15)
    result = sum([opinions[cut+i] for i in range(n-(cut*2))]) / (n-(cut*2))
    result = r(result)
else:
    result = 0
print(result)