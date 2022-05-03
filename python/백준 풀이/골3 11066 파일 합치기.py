#11066 파일 합치기

from sys import stdin

input=stdin.readline

for t in range(int(input())):
        
    k=int(input())
    
    l=list(map(int,input().split()))

    """
    두개씩 합치고
    다른 하나랑 합치고
    제일 적은거부터 합쳐서 
    맨위에 제일 큰 1개 다른 하나
    혹은 합쳐진거 2개씩
    dp[0][1]=0부터 1 까지 최소비용
    dp[0][n-1]=가 답이 되게 하는 알고리즘
    점화식
    dp[i][j]=min(dp[i][k]+dp[k+1][j])+s[j]-s[i]+l[i]
    """
    
    dp=[[10001 for i in range(501)]for i in range(501)]
    
    s=[l[0]]
    
    for i in range(1,k):
        
        s.append(l[i]+s[-1])
    
    def solve(i,j):
    
        if i==j:
            
            return 0
        
        for k in range(i,j):
       
            dp[i][j]=min(solve(i,k)+solve(k+1,j)+s[j]-s[i]+l[i],dp[i][j])
        
        return dp[i][j]

    for q in range(1,k):
        
        for i in range(k-q):    
            
            j=i+q
            
            dp[i][j]=solve(i,j)
            
    print(dp[0][k-1])