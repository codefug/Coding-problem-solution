#2294 동전 2 정리

from sys import stdin

input=stdin.readline

n,k=map(int,input().split())

coins=[int(input()) for _ in range(n)]

dp=[10001 for _ in range(k+1)]
dp[0]=0

for coin in coins:

    for i in range(coin,k+1):

        if dp[i]>dp[i-coin]+1:

            dp[i]=dp[i-coin]+1

print(dp[k] if dp[k]!=10001 else -1)
