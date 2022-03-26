#10871 X보다 작은 수

n,x=map(int,input().split())

l=list(map(int,input().split()))

ans=[]

for i in range(n):
    
    if l[i]<x:
        ans.append(l[i])
        
for i in range(len(ans)-1):
    
    print(ans[i],end=' ')
    
print(ans[-1])