#1699 제곱수의 합 복습

n=int(input())

dp=[0 for i in range(n+1)]

square = [ j*j for j in range(int(n**.5)+1) ]

for i in range(1,n+1):

    for j in square:

        if j>i:

            break


        else:

            dp[i]=dp[i-j]+1

            
print(dp[n])
