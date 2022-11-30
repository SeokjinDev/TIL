# baekjoon 1015
# https://www.acmicpc.net/problem/1015
# Silver 4

n = int(input())
data = [*map(int, input().split())]
sortedData = sorted(data)
result = []
for i in range(n):
    dataIndex = sortedData.index(data[i])
    result.append(dataIndex)
    sortedData[dataIndex] = -1
[print(i, end=' ')for i in result]