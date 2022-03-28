#1890 점프

import sys

input=sys.stdin.readline

n=int(input())

dp=[[0 for i in range(n)] for j in range(n)]

dp[0][0]=1

for i in range(n):

    d=list(map(int,input().split()))

    for j in range(n):

        if dp[i][j]==0:

            continue

        if i+d[j]<n:

            dp[i+d[j]][j]+=dp[i][j]

        if j+d[j]<n:

            dp[i][j+d[j]]+=dp[i][j]

print(dp[n-1][n-1]//4)
