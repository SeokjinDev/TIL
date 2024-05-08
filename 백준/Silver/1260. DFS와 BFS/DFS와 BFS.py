from collections import deque
n,m,s=map(int, input().split())
g=[[]]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    if g[a]:g[a].append(b)
    else:g[a] = [b]
    if g[b]:g[b].append(a)
    else:g[b] = [a]
for i in g:i.sort()
v,t=[0]*(n+1),[s]
while t:
    d=t.pop()
    if not v[d]:
        print(d, end=' ')
        v[d]=1
        t.extend(g[d][::-1])
print()
v,q=[0]*(n+1),deque([s])
while q:
    d=q.popleft()
    if not v[d]:
        print(d,end=' ')
        v[d]=1
        q.extend(g[d])