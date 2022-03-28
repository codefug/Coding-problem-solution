M=int(input())
N=int(input())
if M==2:
    d=[2]
else:
    d=[]
for i in range(M,N+1):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    print('j:',j)
    if j==i//2:
        d.append(i)
if sum(d)==0:
    
    print(-1)
else:
    print(sum(d))
    print(min(d))
