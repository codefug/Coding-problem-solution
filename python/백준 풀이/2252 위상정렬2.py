n,m=map(int,input().split())

l=[0]*(n+1)

way=[[] for _ in range(n+1)]

for i in range(m):

    a,b=map(int,input().split())

    l[b]+=1

    way[a].append(b)

queue=[]

for i in range(1,len(l)):

    if l[i]==0:

        queue.append(i)

while queue:

    t=queue.pop(0)

    for i in way[t]:

        l[i]-=1

        if l[i]==0:

            queue.append(i)

    print(t,end=' ')

    
