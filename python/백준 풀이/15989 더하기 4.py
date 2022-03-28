
#15989 1,2,3 더하기 4
#1

import sys

input=sys.stdin.readline

t=int(input())

num=[]

for n in range(t):

    num.append(int(input()))

dp=[[],[1,0,0],[1,1,0],[1,1,1]]

for i in range(4,max(num)+1):

    next=[]

    next.append(dp[i-1][0])
    next.append(dp[i-2][1]+dp[i-2][0])
    next.append(dp[i-3][2]+dp[i-3][1]+dp[i-3][0])

    dp.append(next)

#2
import sys
input = sys.stdin.readline

t = int(input())
dp = [1 for i in range(10001)]
lst = []

for _ in range(t):
    lst.append(int(input()))

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for i in lst:
    print(dp[i])
