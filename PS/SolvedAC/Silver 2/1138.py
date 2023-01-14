# baekjoon 1338
# https://www.acmicpc.net/problem/1138
# Silver 2

n = int(input())
nums = [*map(int, input().split())]
check = [[0, i] for i in range(n)]
result = [0 for i in range(n)]
for i in range(n):
    result[check[nums[i]][1]] = i + 1
    del check[nums[i]]
[print(r, end=' ') for r in result]