def f(n,s,m,e):
    if n==1:return print(s,e)
    f(n-1,s,e,m)
    f(1,s,m,e)
    f(n-1,m,s,e)
n=int(input())
print(2**n-1)
if n<21:f(n,1,2,3)