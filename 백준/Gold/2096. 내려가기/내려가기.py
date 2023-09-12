n = int(input())
maxData = [*map(int, input().split())]
minData = [*maxData]
for i in range(n-1):
    data = [*map(int, input().split())]
    maxData = [data[0] + max(maxData[:2]),
               data[1] + max(maxData[:]),
               data[2] + max(maxData[1:])]
    minData = [data[0] + min(minData[:2]),
               data[1] + min(minData[:]),
               data[2] + min(minData[1:])]
print(max(maxData), min(minData))