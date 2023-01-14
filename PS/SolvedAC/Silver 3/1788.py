# baekjoon 1788
# https://www.acmicpc.net/problem/1788
# Silver 3

n = int(input())
fibo = [0, 1]
check = True if n > 0 else False

if n == 0:
    print(0)
    print(0)
else:
    # memory manage
    for i in range(abs(n)):
        fibo.append((fibo[0]+fibo[1]) % 1000000000)
        del fibo[0]

    if not (abs(n) % 2 or check): # minus and odd
        print(-1)
        print(fibo[0])
    else:
        print(1)
        print(fibo[0])