#1978 소수 찾기

n=int(input())

l=list(map(int,input().split()))

dp=[1 for i in range(1001)]
dp[1]=0
dp[0]=0

for i in range(2,33):

    for j in range(i,501):

        if i*j>1000:
            break
        dp[i*j]=0

cnt=0

for i in l:

    if dp[i]==1:

        cnt+=1

print(cnt)
