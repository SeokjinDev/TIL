import sys

stack = [0]
answer = []
can = True
point = 1
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    while point <= num:
        answer.append('+')
        stack.append(point)
        point += 1
    if num == stack[-1]:
        answer.append('-')
        stack.pop()
    else:
        can = False
if can:
    print("\n".join(answer))
else:
    print("NO")