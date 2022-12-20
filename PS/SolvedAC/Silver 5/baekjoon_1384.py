# baekjoon 1384
# https://www.acmicpc.net/problem/1384
# Silver 5

c=1
while 1:
    n=int(input())
    if n==0:break
    temp,check=[],[]
    for i in range(n):
        temp.append(input().split())
        for j in range(1, n):
            if temp[i][j] == 'N':
                check.append([i-j if i-j >= 0 else n+(i-j), i])
    print("Group",c)
    if check:
        for i in check:
            print(f"{temp[i[0]][0]} was nasty about {temp[i[1]][0]}")
    else:
        print("Nobody was nasty")
    c+=1
    print()