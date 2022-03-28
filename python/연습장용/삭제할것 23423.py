def perm(a,q):
    if len(a)==1:
        return [a]
    else:
        result=[]
        for i in a:
            b=a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b,q):
                b.insert(0,i)
                if j not in result:
                    result.append(j)
        q.append(result)
def foranswer(d,yonsan,l):
    k=d[0]
    for i in range(1,len(d)):
        if yonsan[i-1]==0:
            k+=d[i]
        if yonsan[i-1]==1:
            k-=d[i]
        if yonsan[i-1]==2:
            k*=d[i]
        if yonsan[i-1]==3:
            if k>=0:
                k//=d[i]
            else:
                -(-k//d[i])
    if l.count(k)==0:
        l.append(k)
N=int(input())
d=list(map(int,input().split()))
k=list(map(int,input().split()))
yonsan=[]
for i in range(len(k)):
    for j in range(k[i]):
        yonsan.append(i)
l=[]
q=[]
perm(yonsan,q)
print(q)
for i in q:
    foranswer(d,i,l)
print(max(l))
print(min(l))
