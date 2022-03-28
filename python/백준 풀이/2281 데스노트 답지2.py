#2281 데스노트 쉐도잉

'''
1.안 채우고 넘기는 경우의 수
2.채우고 안 넘어가는 경우의 수
3.해당 인덱스가 되면 0으로 만들어줌
'''
import sys

sys.setrecursionlimit(10**6)

n,m=map(int,input().split())

name=[int(input())+1 for i in range(n)]

dp=[[-1 for i in range(m+2)] for j in range(n+1)]

def sol(i,c):

    if i==n: return 0

    if dp[i][c]!=-1: return dp[i][c]

    dp[i][c]=sol(i+1,name[i])+(m+1-c)**2

    if c+name[i]<=m+1:

        dp[i][c]=min(dp[i][c],sol(i+1,name[i]+c))

    return dp[i][c]

print(sol(0,0))
