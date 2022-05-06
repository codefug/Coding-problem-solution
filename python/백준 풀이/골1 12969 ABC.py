#12969 ABC

import sys

input=sys.stdin.readline

n,k=map(int,input().split())

'''
for문으로 할수 있는가?

안됨 왜냐 순서대로 되는게 아님 ㅇㅇ

가지 뻗듯이 나가야함
알아야 하는것
1. a 이전개수
2. b 이전개수
3. 현재 가능한 쌍의 개수
4. 그것이 가능한가의 여부가 답에 필요한 요소

'''

dp=[[[0 for i in range(436)] for i in range(31)] for i in range(31)]

def solve(a,b,t,arr):
   
    if len(arr)==n:
        
        if t==k:
            
            print(arr)
            
            sys.exit(0)

        return

    if dp[a][b][t]:
        
        return
    
    solve(a+1,b,t,arr+'A')
    solve(a,b+1,t+a,arr+'B')
    solve(a,b,t+a+b,arr+'C')
       
solve(0,0,0,'')

print(-1)