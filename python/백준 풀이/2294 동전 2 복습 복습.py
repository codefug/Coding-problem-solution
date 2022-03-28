#2294 동전 2 복습 복습

n,k=map(int,input().split())

money=[int(input()) for i in range(n)]

dp=[100001 for i in range(k+1)]

dp[0]=0

for m in money:
    
    for i in range(m,k+1):
        
        if dp[i]>dp[i-m]+1:
            
            dp[i]=dp[i-m]+1

print(dp[k] if dp[k]!=100001 else -1)
