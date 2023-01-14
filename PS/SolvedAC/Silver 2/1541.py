# baekjoon 1541
# https://www.acmicpc.net/problem/1541
# Silver 2

expre = input().split('-')
temp = []
for i in expre:
    temp.append(sum([*map(int, i.split('+'))]))
result = temp[0]
for i in temp[1:]:
    result -= i
print(result)