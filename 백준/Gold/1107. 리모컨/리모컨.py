n = int(input())
m = int(input())
brokens = [*input().split()] if m else []
cnt = abs(100-n)
for num in range(1000000):
    for i in str(num):
        if i in brokens:
            break
    else:
        cnt = min(cnt, abs(num-n)+len(str(num)))
print(cnt)