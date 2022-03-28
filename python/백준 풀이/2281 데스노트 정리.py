#2281 데스노트 다시 해봐

import sys

sys.setrecursionlimit(10**6)

n,m=map(int,input().split())

name=[int(input())+1 for i in range(n)]

"""
필요한것 가로줄 인덱스 세로줄(몇번째 줄인지 몰라도 됨)
"""

dp=[[1001 for i in range(m+1)] for j in range(n+1)]

def f(index,horizon):

    if index==n:

        return 0

    if dp[index][horizon]!=1001:

        return dp[index][horizon]

    if index!=0:
    
        dp[index][horizon]=f(index+1,name[index]-1)+(m-horizon)**2

    if horizon+name[index]<=m:

        dp[index][horizon]=min(dp[index][horizon],f(index+1,horizon+name[index]))

    return dp[index][horizon]

"""
-1로 설정 시작했을 경우
1. 다음줄로 넘어가는 경우에서 horizon에 -1설정 해줘야함 - 해결
2. 인덱스가 처음일때 m- -1되는 문제 - 해결
3. min을 돌렸을때 처음에 하면 0이라서 무조건 전꺼로 되는 문제 - 해결
4. 1001로 만들면 dp[index][horizon]으로 되는 문제- 해결
"""

print(f(0,-1))
