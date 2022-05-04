#12969 ABC

n,k=map(int,input().split())

'''

https://hjp845.tistory.com/165
dp[a][b][쌍의 개수]=0 or 1가 맞고

a b c 하나씩 넣는거 시작

dp[a][b][]         

for문으로 할수 있는가?

안됨 왜냐 순서대로 되는게 아님 ㅇㅇ

가지 뻗듯이 나가야함
'''

def solve(i,a,b,t):
    
    if t==n:
        
        if i==k:
            
            return 1
        
        else:
            
            return 0
        
    if dp[i][a][b][t]:
        
        return 0
    
    