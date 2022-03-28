#16195 1,2,3 더하기 9
import sys

input=sys.stdin.readline

t=int(input())

order=[list(map(int,input().split())) for i in range(t)]

m=max(order)[0]

dp=[[0 for i in range(j)] for j in range(m+1)]

dp[1]=[1]
dp[2]=[1,1]
dp[3]=[1,2,1]

for i in range(4,len(dp)):

    for j in range(1,i):

        if i-3>=j:
            
            dp[i][j]=(dp[i-1][j-1]+dp[i-2][j-1]+dp[i-3][j-1])%1000000009

        elif i-2>=j:

            dp[i][j]=(dp[i-1][j-1]+dp[i-2][j-1])%1000000009

        elif i-1>=j:

            dp[i][j]=(dp[i-1][j-1])%1000000009
            
for c in order:

    n,m=c

    print(sum(dp[n][:m])%1000000009)
