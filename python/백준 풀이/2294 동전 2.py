n,k=map(int,input().split())

money=[]

for i in range(n):

    money.append(int(input()))

dp=[10001 for i in range(k+1)]

dp[0]=0

#dp[1]은 1을 m을 이용해서 만든수 중에 최소값 dp[2]도 같음

for m in money:
    
    a=0
    
    for i in range(m,k+1):
        
        a=dp[i-m]+1
        
        if a<dp[i]:
            
            dp[i]=a
            
print(dp[k])
