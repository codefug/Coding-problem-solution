import random
N=int(input("난수의 개수 입력:"))
l=[]
for i in range(N):
    l.append(random.randint(1,N))
l.sort()
print("리스트:",l)
i=1
m=[l[0]]
M=0
while i<N:
    j=i
    while j<N and l[j-1]+1==l[j]:
        m.append(l[j])
        j+=1
    else:
        j+=1
    print(m)
    if M<len(m):
        M=len(m)
    i=j
print("최장 연속 순차의 길이:",M)
