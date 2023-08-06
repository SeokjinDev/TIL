from sys import stdin
n = int(input())
stack = []
for _ in range(n):
    command = [*map(int, stdin.readline().split())]
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        print(stack.pop() if stack else -1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        print(0 if stack else 1)
    elif command[0] == 5:
        print(stack[-1] if stack else -1)