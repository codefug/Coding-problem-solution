#17070 파이프 옮기기 1 답지 복습

n=int(input())

house=[list(map(int,input().split())) for i in range(n)]

dp=[[[0]*3 for i in range(n)] for i in range(n)]

#0:가로 1:세로 2:대각선

dp[0][1][0]=1

for x in range(2,n):

    if house[0][x]==0:

        dp[0][x][0]+=dp[0][x-1][0]

for y in range(1,n):

    for x in range(2,n):

        if house[y][x]== house[y-1][x] == house[y][x-1] ==0:

            dp[y][x][2]=dp[y-1][x-1][0]+dp[y-1][x-1][1]+dp[y-1][x-1][2]

        if house[y][x]==0:

            dp[y][x][0]=dp[y][x-1][2]+dp[y][x-1][0]

            dp[y][x][1]=dp[y-1][x][2]+dp[y-1][x][1]

print(sum(dp[-1][-1]))
        
