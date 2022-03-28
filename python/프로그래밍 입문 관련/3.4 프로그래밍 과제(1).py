import random
N=int(input("난수의 개수 입력:"))
l=[]
for i in range(N):
    r=random.randint(1,N)
    l.append(r)
print("리스트:",l)
l.sort
g=set(l)
print("집합:",g)
i=1
c=[]
while i<=N:
    G=[]
    j=i
    while j in g:
        G.append(j)
        j+=1
    else:
        i=j
        i+=1
    if len(G)>len(c):
        c=G
print("최장 연속 순차의 길이:",len(c))
print("최장 연속 순차:",c)
