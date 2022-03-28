#9095 1,2,3 더하기 정리

import sys

input=sys.stdin.readline

t=int(input())

order=[]

for i in range(t):

    order.append(int(input()))

dp=[i for i in range(3)]

dp[0]=1

for i in range(3,max(order)+1):
    
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

for num in order:

    print(dp[num])
