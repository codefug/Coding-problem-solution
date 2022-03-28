import random
def merge(r1,r2):
    r3=r1+r2
    r3.sort()
    return  r3

n=int(input("리스트의 원소 개수 입력:"))
t=[]
for i in range(n):
    r=random.randint(1,100)
    t.append(r)
print("최초 리스트:",t)
i=1
RUN=[]
T=[]
RUN.append(t[0])
while i<len(t):
    if t[i]>t[i-1]:
        RUN.append(t[i])
    else:
        T.append(RUN)
        if i<len(t)-1:
            i+=1
        RUN=[t[i]]
print("초기 런 생성:",T)
l=len(T)
while l!=1:
    for i in range(0,l,2):
        T[i]=merge(T[i],T[i+1])
        T.remove(T[i+1])
    l=len(T)
    print("런 합병 단계 :",T)
print("정렬된 리스트:",T)
    
