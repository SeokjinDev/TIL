gradeTable = {'A+': 4.5,
              'A0': 4.0,
              'B+': 3.5,
              'B0': 3.0,
              'C+': 2.5,
              'C0': 2.0,
              'D+': 1.5,
              'D0': 1.0,
              'F': 0}
s1, s2 = 0, 0
for _ in range(20):
    name, credit, grade = input().split()
    credit = float(credit)
    if grade != 'P':
        s1 += credit*(gradeTable[grade])
        s2 += credit
print("%.6f" % (s1/s2))
