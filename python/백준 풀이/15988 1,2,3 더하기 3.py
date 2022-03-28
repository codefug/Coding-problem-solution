#15988 1,2,3 더하기 3

t=int(input())

test=[]

for i in range(t):

    test.append(int(input()))

m=max(test)

dp=[1 for i in range(m+1)]

dp[2]=2

for i in range(3,m+1):

    dp[i]=dp[i-3]%1000000009+dp[i-2]%1000000009+dp[i-1]%1000000009

for i in range(t):

    print(dp[test[i]]%1000000009)

    
