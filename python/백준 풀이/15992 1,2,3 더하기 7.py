#15992 1,2,3 더하기 7

import sys

input=sys.stdin.readline

t=int(input())

order=[list(map(int,input().split())) for i in range(t)]

dp=[[0 for j in range(i)] for i in range(max(order)[0]+1)]

maximum=0

order.sort(key=lambda x:x[1])

maximum=order[-1][1]

dp[1]=[1]
dp[2]=[1,1]
dp[3]=[1,2,1]

p=1000000009

'''
아이디어

dp[i][j]=dp[i-1][j]+dp[i-2][j]+dp[i-3][j]

'''

for i in range(4,len(dp)):

    for j in range(1,maximum):

        if j>len(dp[i])-1:

            break

        if i-3>=j:
            
            dp[i][j]=dp[i-1][j-1]%p+dp[i-2][j-1]%p+dp[i-3][j-1]%p

        elif i-2>=j:

            dp[i][j]=dp[i-1][j-1]%p+dp[i-2][j-1]%p

        elif i-1>=j:

            dp[i][j]=dp[i-1][j-1]%p

        dp[i][j]%=p

for i in order:

    n,m=i

    print(dp[n][m-1]%p)
