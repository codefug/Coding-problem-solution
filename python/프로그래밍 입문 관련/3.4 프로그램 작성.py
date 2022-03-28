import random
N=int(input("난수의 개수입력:"))
l=[]
for i in range(N):
    r=random.randint(1,N)
    l.append(r)
print("리스트:",l)
l.sort
s=set(l)
print("집합:",s)
i=1
G=0
while i<=N:
    g=set()
    for j in range(i,N+1):
        if j in s:
            g.add(j)
        else:
            if G<len(g):
                G=len(g)
                i=j-1
            break
    i+=1
print("최장 연속  순차의 길이:",G)
