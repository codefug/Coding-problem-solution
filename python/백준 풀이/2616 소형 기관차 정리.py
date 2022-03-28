#2616 소형 기관차 정리

n=int(input())

people=list(map(int,input().split()))

m=int(input())

cumsum=[0]

value=0

for p in people:

    value+=p

    cumsum.append(value)

dp=[[0]*(n+1) for _ in range(4)]

for i in range(1,4):

    for j in range(i*m,n-((3-i)*m)+1):

        if i==1:

            dp[i][j]=max(dp[i][j-1],cumsum[j]-cumsum[j-m])

        else:

            dp[i][j]=max(dp[i][j-1],dp[i-1][j-m]+cumsum[j]-cumsum[j-m])

print(dp[3][n])
