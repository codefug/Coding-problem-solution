def merge(r1,r2):
    r3=r1+r2
    r3.sort()
    return r3





import random
n=int(input("리스트의 원소 개수 입력:"))
t=[]
for i in range(n):
    r=random.randint(1,n)
    t.append(r)
print("최초 리스트:",t)
i=0
T=[]
line=[]
while i<len(t):
    j=i
    T.append(t[j])
    j+=1
    while j<len(t) and t[j]>t[j-1]:
        T.append(t[j])
        j+=1
    
