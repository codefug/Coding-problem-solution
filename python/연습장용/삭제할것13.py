import random
n=int(input("리스트의 원소 개수 입력:"))
t=[]
for i in range(n):
    r=random.randint(1,100)
    t.append(r)
print(t)
i=0
q=1
while i<=n-1:
    m=[]
    j=i
    m.append(str(t[j]))
    j+=1
    while j<=n-1 and t[j]>t[j-1]:
        m.append(str(t[j]))
        j+=1
    i=j
    print('run%d :'%(q),' '.join(m))
    q+=1 
    
