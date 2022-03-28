#15988 1,2,3 더하기 3 복습

import sys

input=sys.stdin.readline

t=int(input())

order=[int(input()) for i in range(t)]

dp=[1 for i in range(max(order)+1)]

dp[2]=2

for i in range(3,len(dp)):

    dp[i]=dp[i-1]%1000000009+dp[i-2]%1000000009+dp[i-3]%1000000009

for c in order:

    print(dp[c]%1000000009)
