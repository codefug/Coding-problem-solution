#2281 데스노트 해보자

n,m=map(int,input().split())

number=[int(input()) for i in range(n)]

dp=[-1 for i in range(n)]

k=0

for i in range(n-1,-1,-1):

    k+=number[i]

    if k<=m:

        dp[i]=0

    else:

        k=i

        break

for i in range(k,-1,-1):

    for j in range(n-i-1):

        if sum(number[i:i+j+1])+j <= m:

            dp[i]=min([(m-(sum(number[i:i+j+1])-j))**2+dp[i+j+1]])
                       
print(dp[0])
