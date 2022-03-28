#12865 평범한 배낭 정리

#1
'''
음 dp에 v를 저장하는게 좋을듯 v 자체의 값이 최대여야 되니깐..
처음 설정은 -1 로 해놓고 탐색하면 0 무게만 인덱스로 놓기에는 넣다 뺏다도 해야되고 중복되도 안된다.
고로 몇번째 물건을 보냐로 순서대로 해놓고 이전꺼로 탐색하는데 전의 무게랑 지금 보는 무게 더해도 안 넘으면 넣기 이런거 하면 될듯
'''

import sys

input=sys.stdin.readline

n,k=map(int,input().split())

dp=[[-1 for i in range(k+1)] for i in range(n)]

weight,value=[],[]

for i in range(n):

    w,v=map(int,input().split())

    if w>k:

        n-=1

        continue
    
    weight.append(w)

    value.append(v)

if weight:

    dp[0][weight[0]]=value[0] 
    
    for i in range(1,n):
    
        dp[i][weight[i]]=max(dp[i-1][weight[i]],value[i])

        for j in range(k+1):

            dp[i][j]=max(dp[i-1][j],dp[i][j])

            if dp[i-1][j]!=-1 and j+weight[i]<=k:

                dp[i][j+weight[i]]=max(dp[i-1][j+weight[i]],dp[i-1][j]+value[i])

    print(max(dp[n-1]))

else:

    print(0)
#2
from sys import stdin
input = stdin.readline

def dp(N,K):
    D = {0:0}

    for _ in range(N):
        w,c = map(int, input().split())
        tmp = {}

        for dw,dc in D.items():
            neww = w+dw; newc = c+dc
            if neww <= K and newc > D.get(neww,0):
                tmp[neww] = newc
        D.update(tmp)
    
    return max(D.values())

N,K = map(int, input().split())
D = dp(N,K)
print(D)
