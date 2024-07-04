def solution(arr):
    stack = [arr[0]]
    for a in arr[1:]:
        x = stack.pop()
        stack.append(x)
        if x != a:
            stack.append(a)
    return stack