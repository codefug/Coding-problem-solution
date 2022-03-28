#12869 뮤탈리스크

from itertools import permutations

num=int(input())

scv=list(map(int,input().split()))

dp=[[[61 for u in range(scv[2]+1)] for i in range(scv[1]+1)] for o in range(scv[0]+1)]

three_cusion=[-9,-3,-1]

def solution(a,b,c):

    if dp[a][b][c]!=61:

        return dp[a][b][c]

    if a==b==c==0:

        return 0

    for q,w,e in permutations(three_cusion,3):

        dp[a][b][c]=min(dp[a][b][c],1+solution(max(0,a+q),max(0,b+w),max(0,c+e)))

    return dp[a][b][c]

print(solution(scv[0],scv[1],scv[2]))
