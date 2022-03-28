#2281 데스노트 해보자

import sys
sys.setrecursionlimit(10**6)
#파이썬 재귀 제한 해제

n,m=map(int,input().split())
#n,m입력

names=[int(input())+1 for _ in range(n)]
#names 리스트 작성 : 뒤쪽의 빈칸을 남겨야 하기때문에 +1 로 세트로 모음

dp=[[-1 for _ in range(m+2)] for _ in range(n+1)]
#visited리스트 작성, 값도 입력
#m+2인 이유는 names에서 1을 +해서 받았는데 계산할때만 이를 다시 빼기 때문이다.

def solution(i,col):
    if i==n: return 0
#마지막 인덱스가 나온곳은 무조건 마지막 줄인것이므로 0 리턴

    if dp[i][col]!=-1: return dp[i][col]
#visit되었다면 저장된 값 출력
#visited를 하는 이유는 이전것과 상관없이 이 자리에 왔을때 이후의 것을 판단해서 값을 넣기 때문.
#dp[i]는 i+1부터 끝값까지 최적화된 값을 넣어놓은 것이다.

    dp[i][col]=solution(i+1,names[i])+(m+1-col)**2
#처음에 줄을 바로 넘어가는 경우의 수로 재귀, 이후에는 현재 줄에서 다음줄로 넘어가는 경우의 수

    if col+names[i]-1 <=m:
#col+names[i] 즉 현재 모여있는것과 name을 가져왔을때 그러니깐 합쳣을때 그 줄을 넘지 않을경우

        dp[i][col]=min(dp[i][col],solution(i+1,col+names[i]))
#dp는 이전에 넘어가는 경우의 수 와 지금 줄을 넘어가지않은 경우의 수 중에서 더 낮은걸로 저장된다

#이것은 재귀로써 반복된다.
    return dp[i][col]
#리턴

print(solution(0,0))
#답
