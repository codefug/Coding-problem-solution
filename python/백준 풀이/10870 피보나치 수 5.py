# 10870 피보나치 수 5 정리

n=int(input())

dp=[0 for i in range(21)]

dp[1]=1

for i in range(2,21):

    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])
