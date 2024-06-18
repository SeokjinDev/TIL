data = []
for c in input():
    if c in ['U', 'C', 'P']:
        data.append(c)

def check(data):
    index = 0
    for i in range(len(data)):
        if data[i] == 'U' and index == 0:
            index += 1
        elif data[i] == 'C' and index == 1:
            index += 1
        elif data[i] == 'P' and index == 2:
            index += 1
        elif data[i] == 'C' and index == 3:
            index += 1
    return index

if check(data) == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")