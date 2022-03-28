#1806 부분합 정리
from sys import stdin

input=stdin.readline

n,s=map(int,input().split())

l=list(map(int,input().split()))

answer=100000001

dp=[0 for i in range(n+1)]

dp[1]=l[0]

start_point=0

end_point=1

for i in range(2,n+1):

    dp[i]=dp[i-1]+l[i-1]

while start_point<=n:

    print(start_point,end_point)

    if dp[end_point]-dp[start_point]>=s:

        if end_point-start_point<answer:

            answer=end_point-start_point

        start_point+=1
        
    else:

        if end_point==n:

            start_point+=1

        else:
            
            end_point+=1
            
if answer==100000001:

    print(0)

else:
    print(answer)
