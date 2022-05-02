#11066 파일 합치기

import sys

input=sys.stdin.readline

T=int(input())

for t in range(T):
    
    fn=int(input())
    
    fl=list(map(int,input().split()))

    sum=[0]
    
    for i in range(fn):
        
        sum.append(sum[-1]+fl[i])
    #sum[i]는 fn[i]까지 다 더한 값
    
    dp=[[0 for i in range(fn+1)] for i in range(fn+2)]
    
    knuth=[[0 for i in range(fn+1)] for i in range(fn+1)]
    
    for i in range(1,fn+1):
        knuth[i][i]=i

    for d in range(1,fn):
        
        for i in range(1,fn-d+1):
            
            j=i+d
            
            dp[i][j]=int(1e10)
            
            for k in range(knuth[i][j-1],knuth[i+1][j]+1):
                
                tmp=dp[i][k]+dp[k+1][j]+sum[j]-sum[i-1]
                
                if tmp<dp[i][j]:
                    
                    dp[i][j]=tmp
                    
                    knuth[i][j]=k
            
    print(dp[1][fn])