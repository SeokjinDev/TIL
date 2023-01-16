# baekjoon 18870
# https://www.acmicpc.net/problem/18870
# Silver 2

from sys import stdin

class mergeSort():
    def __init__(self, data):
        self._data = data
    def _merge(self, data, left, mid, right):
        Lidx, Ridx = left, mid+1
        sortlist = []
        while Lidx <= mid and Ridx <= right:
            if data[Lidx] <= data[Ridx]:
                sortlist.append(data[Lidx])
                Lidx += 1
            else:
                sortlist.append(data[Ridx])
                Ridx += 1
        if(Lidx > mid):
            for i in range(Ridx, right+1):
                sortlist.append(data[i])
        else:
            for i in range(Lidx, mid+1):
                sortlist.append(data[i])
        self._data[left:right+1] = sortlist
    def _mergeSort(self, data, left, right):
        if left < right:
            mid = (left + right) // 2
            self._mergeSort(data, left, mid)
            self._mergeSort(data, mid+1, right)
            self._merge(data, left, mid, right)
    def get(self):
        self._mergeSort(self._data, 0, len(self._data)-1)
        return self._data

N = int(stdin.readline())
data = list(map(int, stdin.readline().split()))
mixedData = list(set(data))     # Remove duplicate data
m = mergeSort(mixedData)
dataIndex = {}
sortedData = m.get()
for d, i in zip(sortedData, range(N)):
    try:
        if dataIndex[d]:
            pass
    except:
        dataIndex[d] = i
for i in data:
    print(dataIndex[i], end=' ')