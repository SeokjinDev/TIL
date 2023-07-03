n = int(input())
grades = [*map(int, input().split())]
maxNum = max(grades)
print(sum([grades[i]/maxNum*100 for i in range(n)]) / n)