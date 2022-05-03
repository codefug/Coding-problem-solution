#10942 팰린드롬

from sys import stdin

input=stdin.readline

'''
자연수 n 질문 m
각질문 두정수 s e
s부터 e까지 수가 팰린드롬이냐
이다 아니다 대답
1 2 1 3 1 2 1 이면
1 3 은 121이 이다
2 5 은 2131 이 아니다
3 3 이면 1은 이다.
5 7 이면 121은 이다.
'''

n=int(input())
#n 입력

l=[0]+list(map(int,input().split()))
#문제 특성상 그냥 1번째 파일 이렇게 하는게 편할것 같아 인덱스 = 숫자로 만듬 [0]더해서

m=int(input())
#m 입력

q=[]
for i in range(m):    
    q.append(list(map(int,input().split())))
# 질문 입력        

dp=[[0 for i in range(n+1)] for i in range(n+1)]
# dp리스트

for d in range(n):
    for i in range(1,n-d+1):
        j=i+d
        # 차이 0부터 끝까지 하나씩 탐색
        
        if i==j:    
            dp[i][j]=1
        # 차이가 없으면 같으므로 1리턴
            
        elif l[i]==l[j]:
            if i+1==j:
                dp[i][j]=1
            # 1차이 날때 둘이 같으면 1리턴
                
            elif dp[i+1][j-1]==1:
                dp[i][j]=1
            # 그 이상 차이 날때 그 이전의 것(양쪽에서 1씩 범위가 줄어든 dp)
            # 이 1이면 1리턴
                
for i in q:
    
    print(dp[i[0]][i[1]])
#답!
    
# 최적화 코드

import sys
import functools
input=sys.stdin.readline
# 스탠다드 인풋

def sol():
    
    n=int(input())
    # n 입력
    
    sequence=list(map(int,input().split()))
    # 리스트 입력
    
    m=int(input())
    # m 입력
    
    ans=[]
    # answer 생성
    
    @functools.lru_cache(maxsize=None)
    # 제한없이 캐시 최대값제한을 풀고 같은 요청이 왔을때 캐시를 리턴
    
    def check(s,e):
        
        tmp=sequence[s-1:e]
        #인덱스값으로 s부터 e까지의 리스트
        
        if tmp==tmp[::-1]:
        # 현재 리스트가 거꾸로 리스트랑 같으면
            
            return '1'
        # 1리턴
        
        return '0'
        # 0리턴

    print('\n'.join(check(*map(int,input().split())) for i in range(m)))
    # '\n' 을 하나씩 넣으면서 리턴

sol()