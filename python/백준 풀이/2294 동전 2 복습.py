#2294 동전 2 복습 dp

n,k=map(int,input().split())

l=[int(input()) for i in range(n)]

dp=[10001 for i in range(k+1)]

dp[0]=0

for coin in l:
    
    a=0
    
    for i in range(coin,k+1):

        a=dp[i-coin]+1

        if dp[i]>a:

            dp[i]=a

print(dp[k] if dp[k]!=10001 else -1)
