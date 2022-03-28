#15988 1,2,3 더하기 3

import sys

input=sys.stdin.readline

t=int(input())

order=[int(input()) for i in range(t)]

dp=[i for i in range(3)]

dp[0]=1

for c in range(3,max(order)+1):

    dp.append(dp[c-1]%1000000009+dp[c-2]%1000000009+dp[c-3]%1000000009)

for i in order:

    print(dp[i]%1000000009)
