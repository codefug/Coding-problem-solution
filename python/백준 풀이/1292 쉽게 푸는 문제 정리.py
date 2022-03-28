#1292 쉽게 푸는 문제 정리

a,b=map(int,input().split())

dp=[0 for i in range(1001)]

i=1

j=1

while i!=1001:

    dp[i]=j

    i+=1

    if dp.count(j)==j:

        j+=1

print(sum(dp[a:b+1]))
