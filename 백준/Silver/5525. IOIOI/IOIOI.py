n = int(input())
m = int(input())
s = [*input()]
c = 'I' + ('OI' * n)
l = 2*n+1
count = 0
while len(s) >= l:
    if ''.join(s[:l]) == c:
        count += 1
        del s[0:2]
    else:
        del s[0]
print(count)