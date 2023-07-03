while 1:
    num = input()
    if num == '0':
        break
    print("yes" if num == ''.join([*reversed(num)]) else "no")