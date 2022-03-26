#11049 행렬 곱셈 순서

n=int(input())

graph=[]

for i in range(n):
    
    graph.append(list(map(int,input().split())))

dp=[[0]*n for _ in range(n)]

for i in range(1,n):
    #i는 시작값
    for j in range(n-i):
        #j는 움직이는 값
        
        x=i+j
        #x는 시작값+움직이는 값
        
        dp[j][x]=2**32
        #최댓값으로 해야 최솟값으로 일반화하기 편함
        
        for k in range(j,x):
            
            dp[j][x]=min(dp[j][x],dp[j][k]+dp[k+1][x]+graph[j][0]*graph[k][1]*graph[x][1])

print(dp[0][n-1])
