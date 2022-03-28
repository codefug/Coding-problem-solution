#11049 행렬 곱셈 순서

n=int(input())

graph=[]

for_in range(n):

    graph.append(list(map(int,input().split())))

dp=[[0]*n for _ in range(n)]

for i in range(1,n):

    for j in range(n-i):

        x=i+j

        dp[j][x]=2**32

        for k in range(j,x):

            
