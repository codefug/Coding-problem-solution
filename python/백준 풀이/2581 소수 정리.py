#2581 소수 정리

m=int(input())
n=int(input())

dp=[1 for i in range(10001)]
dp[0],dp[1]=0,0
sum_answer=0
min_answer=0

for i in range(2,101):
    for j in range(i,5001):
        if i*j>10000:
            break
        if dp[i*j]==1:
            dp[i*j]=0

for i in range(m,n+1):
    if dp[i]==1:
        if min_answer==0:
            min_answer=i
        sum_answer+=i
if min_answer:
    print(sum_answer)
    print(min_answer)
else:
    print(-1)
