n,m=map(int,input().split())

l=[[] for _ in range(n+1)]

lcount=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    lcount[b]+=1
    l[a].append(b)

queue=[]

for i in range(1,len(lcount)):
    if lcount[i]==0:
        queue.append(i)

while queue:
    t=queue.pop(0)
    for i in l[t]:
        lcount[i]-=1
        if lcount[i]==0:
            queue.append(i)
    print(t,end=' ')
