try:
    while 1:
        s = input()
        while 'BUG' in s:
            s = s.replace('BUG', '')
        print(s)
except:
    pass