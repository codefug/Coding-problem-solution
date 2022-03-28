M=int(input())
N=int(input())
d=[]
for i in range(M,N+1):
    k=0
    for j in range(2,i//2+1):
        if i%j==0:
            k=1
    if k==0:
        d.append(i)
if d.count(1)==1:
    d.remove(1)
if len(d)==0:
    print(-1)
else:
    print(d)
    print(sum(d))
    print(min(d))
