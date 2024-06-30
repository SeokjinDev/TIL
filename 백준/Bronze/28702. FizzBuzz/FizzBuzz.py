for i in range(3):
    if (a:=input()).isnumeric():
        r = int(a)+(3-i)
if r % 3 == 0 or r % 5 == 0:
    if r % 3 == 0:
        print("Fizz", end='')
    if r % 5 == 0:
        print("Buzz", end='')
else:
    print(r)