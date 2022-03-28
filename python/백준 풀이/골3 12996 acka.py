#12996 acka

s,a,b,c=map(int,input().split())

dp=[[[[-1 for q in range(c+1)] for w in range(b+1)] for e in range(a+1)] for r in range(s+1)]

def solution(n,a,b,c):
    
    if n==0:
        
        if a==0 and b==0 and c==0:
        
            return 1
        
        else:
            
            return 0
        
    if a<0 or b<0 or c<0:
        
        return 0
    
    if dp[n][a][b][c]!=-1:
        
        return dp[n][a][b][c]
    
    dp[n][a][b][c]=0
    
    for q in range(2):
        
        for w in range(2):
        
            for e in range(2):
        
                if q==w==e==0:
                    
                    continue
                
                dp[n][a][b][c]+=solution(n-1,a-q,b-w,c-e)
    
    dp[n][a][b][c]%=1000000007
    
    return dp[n][a][b][c]

print(solution(s,a,b,c))