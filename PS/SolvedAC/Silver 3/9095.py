# baekjoon 9095
# https://www.acmicpc.net/problem/9095
# Silver 3

for _ in range(int(input())):
    check = [1, 2, 4]
    n = int(input())
    for i in range(3, n):
        check.append(check[i-1]+check[i-2]+check[i-3])
    print(check[n-1])