n = int(input())
m = int(input())
nums = [0] * (n+1)
for i in range(2, n+1):
    if nums[i] == 0:
        for j in range(i, n+1, i):
            if j % i == 0:
                nums[j] = max(nums[j], i)
ans = sum([1 if i <= m else 0 for i in nums])-1
print(ans)