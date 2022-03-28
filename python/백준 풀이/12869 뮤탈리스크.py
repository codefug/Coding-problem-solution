#12869 뮤탈리스크

from itertools import permutations

n=int(input())

scv=list(map(int,input().split()))

three_cusion=[-9,-3,-1]

while len(scv)!=3:

    scv.append(0)
#고민 많이 했는데 0 을 더 넣으면 되는 거였음
"""
조건
1. scv 인덱스
2. scv 체력
"""
dp=[[[61 for i in range(scv[2]+1)] for j in range(scv[1]+1)] for q in range(scv[0]+1)]

answer=61

def solution(a,b,c):

    if a==b==c==0:

        return 0

    if dp[a][b][c]!=61:

        return dp[a][b][c]

    for q,w,e in permutations(three_cusion,3):

        dp[a][b][c]=min(dp[a][b][c],1+solution(max(0,a+q),max(0,b+w),max(0,c+e)))

    return dp[a][b][c]

print(solution(scv[0],scv[1],scv[2]))
