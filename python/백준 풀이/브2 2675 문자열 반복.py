#2675 문자열 반복

T=list(map(int,input().split()))
ans=[]
for i in range(len(T)):
    
    num,str=input().split()
    num=int(num)
    answer=""
    for j in range(len(str)):
        for n in range(num):
            answer+=str[j]
    ans.append(answer)
    
for i in range(len(ans)):
    print(ans[i])
