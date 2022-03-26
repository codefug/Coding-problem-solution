#12996 Acka

from math import factorial

s,a,c,k=int(input())

if a+c+k<s:

    print(0)

elif a+c+k==s:

    print(factorial(s))

else:
    '''
    1. 남은 곡
    2. 남은 기회
    3. 방법 수
    4. 사람마다 다름
    '''
    def solution(a,c,k,s):
        '''
        이거는 이제 재귀 함수로 할건데 
        direct를 계속 돌리면서 재귀할거임 +1 해 주면서
        
        '''
    dp=[[[[-1 for i in range(s)] for q in range(k)] for w in range(c)] for e in range(k)]
    '''
    dp[첫번째 사람][두번째 사람][세번째 사람][곡의 수]=방법수
    마지막에 답은
    dp[0][0][0][0]에 다 저장될 예정
    '''
    direct=[(0,0,-1),(0,-1,0),(-1,0,0),(0,-1,-1),(-1,-1,0),(-1,0,-1),(-1,-1,-1)]
    
    
    
    print(solution(a,c,k,s))