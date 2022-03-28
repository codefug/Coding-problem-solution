#1806 부분합 정리

n,s=map(int,input().split())

order=list(map(int,input().split()))

answer=100000001

dp=[0 for i in range(n+1)]

for i in range(1,n+1):

    dp[i]=dp[i-1]+order[i-1]

start=0

end=1

while start!=n:

    if dp[end]-dp[start]>=s:

        if answer>end-start:

            answer=end-start

        start+=1

    else:

        if end==n:

            start+=1

        else:

            end+=1

print(answer)
