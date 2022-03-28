n,s=map(int,input().split())
li=list(map(int,input().split()))
answer=100000001

start=0
end=1

sum_li=[0]*(n+1)

for i in range(1,n+1):
    sum_li[i]=li[i-1]+sum_li[i-1]
    
while start!=n:
    if sum_li[end]-sum_li[start]>=s:
        if end-start<answer:
            answer=end-start
        start+=1
    else:
        if end!=n:
            end+=1
        else:
            start+=1

if answer==100000001:
    print(0)
else:
    print(answer)
