#15989 1,2,3 더하기 4

#1

import sys

input=sys.stdin.readline

t=int(input())

order=[int(input()) for i in range(t)]
'''
dp=[1 for i in range(max(order)+1)]

for i in range(2,len(dp)):

    dp[i]+=dp[i-2]

for i in range(3,len(dp)):

    dp[i]+=dp[i-3]

for t in order:

    print(dp[t])
'''

#2

dp=[[],[1,0,0],[1,1,0],[1,1,1]]

for i in range(4,max(order)+1):

    answer=[]

    answer.append(dp[i-1][0])

    answer.append(dp[i-2][0]+dp[i-2][1])

    answer.append(dp[i-3][0]+dp[i-3][1]+dp[i-3][2])

    dp.append(answer)

for t in order:

    print(sum(dp[t]))
