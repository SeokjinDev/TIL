x = int(input())
count = 0
if x % 2:
    count += 1
    x -= 1
for i in range(6):
    if x >= 2**(6-i):
        x -= 2**(6-i)
        count += 1
print(count)