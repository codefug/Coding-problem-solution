#2281 데스노트 최적화 코드 답지

import sys

sys.setrecursionlimit(10**6)

n,m=map(int,input().split())

names=[int(input())+1 for _ in range(n)]

dp=[[-1 for _ in range(m+2)] for _ in range(n+1)]

def solution(i,col):

    if i==n: return 0
    
    if dp[i][col]!=-1: return dp[i][col]

    dp[i][col]=solution(i+1,names[i])+(m+1-col)**2

    if col+names[i] <=m+1:

        dp[i][col]=min(dp[i][col],solution(i+1,col+names[i]))

    return dp[i][col]

print(solution(0,0))
