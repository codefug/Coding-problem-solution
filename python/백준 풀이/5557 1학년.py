#5557 1학년 정리

'''
bfs 인데 dp를 사용할 거임. 식은 고정이고 마지막 수 전까지를 식으로 써서 마지막 수가 나와야 되는것.
고로 마지막 수를 먼저 저장을 시킨다음에 dp를 마지막 수 전까지 돌리고 마지막수가 맞는지 확인 후 cnt+1 이런식으로 돌려야 될듯
돌릴때 조건은 i>=0 and i<=20
'''

import sys

input=sys.stdin.readline

n=int(input())

numbers=list(map(int,input().split()))

dp={numbers[0]:1}

answer=numbers[n-1]

for i in range(1,n-1):

    nextdp={}
    
    for number,cnt in dp.items():

        if number+numbers[i]<=20:

            nextdp[number+numbers[i]]=nextdp.get(number+numbers[i],0)+cnt

        if number-numbers[i]>=0:

            nextdp[number-numbers[i]]=nextdp.get(number-numbers[i],0)+cnt

    dp=nextdp

print(dp[answer])
