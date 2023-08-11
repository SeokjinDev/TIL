n = int(input())
nums = sorted([*map(int, input().split())], reverse=True)
m = int(input())
start, end = 0, nums[0]
while start <= end:
    mid = (start+end) // 2
    value = sum([i if i < mid else mid for i in nums])
    if value > m:
        end = mid-1
    else:
        start = mid+1
print(end)