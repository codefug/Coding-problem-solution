#9095 1,2,3 더하기

t=int(input())

order=[int(input()) for i in range(t)]

dp=[1 for i in range(max(order)+1)]

dp[2]=2

for i in range(3,len(dp)):

    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for c in order:

    print(dp[c])
