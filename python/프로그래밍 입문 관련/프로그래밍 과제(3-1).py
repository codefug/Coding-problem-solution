def merge(r1,r2):
    r3=r1+r2
    return r3

import random
n=int(input("리스트의 원소 개수 입력:"))
t=[]
for i in range(n):
    r=random.randint(1,100)
    t.append(r)
print("최초 리스트:",t)
i=0
T=[]
while i<n:
    m=[]
    j=i
    m.append(t[j])
    j+=1
    while j<n and t[j]>t[j-1]:
        m.append(t[j])
        j+=1
    T.append(m)
    i=j
print("초기 런 생성:",T)
t=T
while len(T)!=1:
    i=1
    j=1
    while i<len(T):
        t[j]=(merge(T[i],T[i-1]))
        t[j].sort()
        t.remove(t[j-1])
        i+=2
        j+=1
        print("t:",t)
    T=t
    print("T:",T)
    print("런 합병 단계:",t)
