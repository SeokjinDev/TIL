r = 0
for i in range(3):
    a = input()
    if a.isnumeric():
        r = int(a)+(3-i)

if r % 3 == 0 and r % 5 == 0:
    print("FizzBuzz")
elif r % 3 == 0:
    print("Fizz")
elif r % 5 == 0:
    print("Buzz")
else:
    print(r)