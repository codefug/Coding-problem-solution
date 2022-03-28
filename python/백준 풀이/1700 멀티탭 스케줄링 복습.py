#1700 멀티탭 스케줄링 정리2

def index(l,item):

    if l.count(item)==0:

        return 101

    else:

        return l.index(item)

n,k=map(int,input().split())

item=list(map(int,input().split()))

idx=[]

for i in range(k):

    idx.append(index(item[i+1:],item[i])+i+1)

consent=[]

i=0

while i<=n-1:

    if consent.count(i)!=0:

        consent.remove(i)
        consent.append(idx[i])
        n+=1
        i+=1
    else:

        consent.append(idx[i])
        i+=1
i=n

answer=0

while i<=k-1:

    if consent.count(i)==0:

        consent.remove(max(consent))

        answer+=1

        consent.append(idx[i])

        i+=1

    else:

        consent.remove(i)
        consent.append(idx[i])
        i+=1
print(answer)
