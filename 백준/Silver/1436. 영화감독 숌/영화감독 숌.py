N = int(input())
number = 666
count = 0
while 1:
    if '666' in str(number):
        count += 1
    if N == count:
        print(number)
        break
    number += 1