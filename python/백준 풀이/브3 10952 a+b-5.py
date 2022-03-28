#10952 a+b-5

a,b=map(int,input().split())

ans=[]

while a and b:
    
    ans.append(a+b)
    
    a,b=map(int,input().split())

for i in range(len(ans)):
    
    print(ans[i])