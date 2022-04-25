#14238 골3 출근 기록

from sys import stdin

input=stdin.readline().strip

def solve(a,b,c,p1,p2):
    
    if a<0 or b<0 or c<0:
        
        return False
    
    if a==b==c==0:
        
        return True
    
    if dp[a][b][c][p1][p2]:
        
        return False
    
    dp[a][b][c][p1][p2]=True
    
    ans[n-a-b-c]='A'
    
    if solve(a-1,b,c,0,p1):
        
        return True
    
    if p1!=1:
        ans[n-a-b-c]='B'
        if solve(a,b-1,c,1,p1):
            
            return True
        
    if p1!=2 and p2!=2:
        
        ans[n-a-b-c]='C'
        
        if solve(a,b,c-1,2,p1):
            
            return True
        
    return False

s=input()

n=len(s)

dp=[[[[[0 for i in range(3)]for i in range(3)]for i in range(50)]for i in range(50)]for i in range(50)]

an,bn,cn=0,0,0

ans=[0]*n

for k in s:
    
    if k=="A":
        
        an+=1
        
    elif k=="B":
        
        bn+=1
        
    else:
        
        cn+=1

if solve(an,bn,cn,0,0):
    
    print(''.join(ans[:n]))
    
else:
    
    print(-1)