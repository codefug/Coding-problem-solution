#골3 14238 출근 기록 답지

'''
답지를 본 이유
1. a,b,c의 경우만 살펴보고 다른 요소를 살피지 못함
2. 이 문제의 특성이긴 하지만 a b c 각각의 조건도 dp에 들어가야한다는 걸 배움
3. 문자열로 출력하기 위한 요소도 있어야한다.
4. join 함수로 문자열에 있는걸 쉽게 낼 수 있다.
5. go 함수 안에 느낌들을 좀 보면 Ture False 로 그 이후로 갈지를 결정후 안되면 -1 끝까지 되면 문자열 출력
이런 느낌이라는 걸 알 수 있으며 이 구현법 익힐 것.
'''

from sys import stdin

input=stdin.readline

S = input()
#S 출근 기록 입력

n = len(S)
#n 일자

dp = [[[[[0 for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
#dp[a][b][c][p1][p2]

ans = [0] * 50
#ans = [0 ... 0] 50개 이후에 join 함수를 이용하여 문자열로 출력될 녀석이다

def go(a, b, c, p1, p2):
#go함수 a b c p1 p2 로 돌아감

    if a < 0 or b < 0 or c < 0:
        return False
#만약 쓸 수 있는 날짜를 넘겼다면 False

    if a == 0 and b == 0 and c == 0:
        return True
#다 썼으면 리턴    

    if dp[a][b][c][p1][p2]:
        return False
#탐색했었으면 False    

    dp[a][b][c][p1][p2] = True
#탐색 완료

    ans[n-a-b-c] = 'A'
#ans를 문자열이라고 생각한다. 처음 함수에 들어왔다면 n-a-b-c는 0으로 첫번째 알파벳이 'A'취급된다.    
    
    if go(a - 1, b, c, 0, p1):
        return True
#이전 것이 a인 다음 함수로 이동 되면 True

    if p1 != 1:
        ans[n-a-b-c] = 'B'
        if go(a, b - 1, c, 1, p1):
            return True
#이전 것이 b인 다음 함수로 이동 되면 True
        
    if p1 != 2 and p2 != 2:
        ans[n-a-b-c] = 'C'
        if go(a, b, c - 1, 2, p1):
            return True
#이전 것이 c인 다음 함수로 이동 되면 True

    return False
#통과 안되면 False


an = 0
bn = 0
cn = 0
# ""n은 ""이 나온 개수

for s in S:
    if s == 'A':
        an += 1
    elif s == 'B':
        bn += 1
    elif s == 'C':
        cn += 1
#an bn cn 만들기        

if go(an, bn, cn, 0, 0):
    print(''.join(ans[:n]))
#처음이니깐 p1 p2 는 0 0 이고 an bn cn 을 넣어서 join 함수로 문자열 출력 아니면 -1 출력    
    
else:
    print(-1)