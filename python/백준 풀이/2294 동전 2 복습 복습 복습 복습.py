#2294 동전 2 정리

n,k=map(int,input().split())

coins=[int(input()) for i in range(n)]

dp=[100001 for i in range(k+1)]

dp[0]=0

for coin in coins:

    for i in range(coin,k+1):

        if dp[i]>dp[i-coin]+1:

            dp[i]=dp[i-coin]+1

print(dp[k])
