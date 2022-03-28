n,s=map(int,input().split())
l=list(map(int,input().split()))
sum_l=[0]*n
sum_l[0]=l[0]
for i in range(1,n):
    sum_l[i]=l[i]+sum_l[i-1]
answer=100000001
start=0
end=1
while start!=n-1:
    if sum_l[end]-sum_l[start]>=s:
        if end-start<answer:
            answer=end-start
        start+=1
    else:
        if end!=n-1:
            end+=1
        else:
            start+=1
print(answer if answer!=100000001 else 0)
