#2281 데스노트

import sys

sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
#n,m 입력
name=[int(input()) for i in range(n)]
#이름
dp=[[-1 for i in range(m+1)] for j in range(n)]
#dp생성
    
def solution(index,col):
    
    if index==n: return 0
    #마지막 단어를 탐색할시 0 리턴
    
    if dp[index][col]!=-1: return dp[index][col]
    
    dp[index][col]=solution(index+1,name[index])+(m-col)**2
    
    if col+1+name[index]<=m:
    
        dp[index][col]=min(dp[index][col],solution(index+1,col+1+name[index]))
    
    return dp[index][col]
    
print(solution(0,-1))
