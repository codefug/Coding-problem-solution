#15990 1,2,3 더하기 5

t=int(input())

order=[int(input()) for o in range(t)]

dp=[[],[1,0,0],[0,1,0],[1,1,1]]

for i in range(4,max(order)+1):

    dp.append([dp[i-1][1]%1000000009+dp[i-1][2]%1000000009
                    ,dp[i-2][0]%1000000009+dp[i-2][2]%1000000009
                    ,dp[i-3][0]%1000000009+dp[i-3][1]%1000000009])

for c in order:

    print(sum(dp[c])%1000000009)
