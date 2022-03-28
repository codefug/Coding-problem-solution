#15486 퇴사 2

#1
"""
아이디어

1.plan을 생성

2.dp를 처음부터 돌려서 dp[i+plan[i][0]]를 dp[i]+plan[i][1] 로 만듬 (그 날까지 가는 최소 시간)


"""

n=int(input())
#n 입력

dp=[0 for i in range(n+2)]
#dp 생성 인덱스는 1= 1일차

for i in range(1,n+1):

    t,p=map(int,input().split())

    if dp[i]<dp[i-1]:

        dp[i]=dp[i-1]

    if i+t<=n+1 and dp[i+t]<dp[i]+p:

        dp[i+t]=dp[i]+p
#dp[i+t]=일하고 난 다음날
if dp[n+1]>dp[n]:

    dp[n]=dp[n+1]

print(dp[n])
