#10950 a+b-3

t=int(input())
ans=[]
for i in range(t):
    
    case=list(map(int,input().split()))

    ans.append(case[0]+case[1])
for i in range(len(ans)):
    
    print(ans[i])