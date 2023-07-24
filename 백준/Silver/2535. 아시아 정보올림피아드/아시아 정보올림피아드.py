n = int(input())
students = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: x[2], reverse=True)
con = {}

count = 0
for s in students:
    if con.get(s[0]) is None:
        con[s[0]] = 1
        print(s[0], s[1])
        count += 1
    elif con[s[0]] < 2:
        con[s[0]] += 1
        print(s[0], s[1])
        count += 1
    if count > 2:
        break