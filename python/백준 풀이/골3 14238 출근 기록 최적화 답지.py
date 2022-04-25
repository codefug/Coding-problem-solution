#14238 출근 기록 최적화

def main():
    #시작
    
    global ansl
    #기록의 길이 ansl 전역함수화
    
    a = input()
    #a 입력
    
    ansl = len(a)
    #ansl 기록의 길이
    
    ans = -1
    #ans default 값 -1
    
    cCnt = [0, 0, 0] 
    #a, b, c 기록
    
    for c in a:
        
        cCnt[ord(c) - 65] += 1
    #cCnt ord 함수를 이용해 0 에 A 1에 B 2에 C의 값이 들어가게 설정
        
    for i in range(3):
        #0 1 2 : A B C
        if cCnt[i] > 0:
            #만약 A B C가 나오는 횟수가 각각 0보다 크다면
            
            tmp = getans(i, [cCnt[0], cCnt[1], cCnt[2]])
            #tmp 함수에 돌려서 나오는 값이 tmp가 된다.
            
            if tmp != -1:
                ans = tmp
                break
            #문자열이 출력되면 ans를 문자열로 바꾼다.
            
    print(ans)
    #ans가 바뀌지 않았다면 -1 바뀌었다면 문자열 출력됨
    
def getans(sIdx, cntList):
    
    global ansl
    #똑같이 ansl 전역함수로
    
    word = chr(sIdx + 65)
    #word 기본 설정 첫값으로 (chr(65,66,67)=알파벳A,B,C)
    
    cntList[sIdx] -= 1
    #cntList에서 탐색중인 알파벳 개수 뺌
    #이제 그 알파벳을 넣었다고 생각하는거임
    
    dis = [51, 51, 51] 
    # A로부터 거리, B로부터 거리, C로부터 거리
    
    dis[sIdx] = 0 
    # 이전 알파벳을 이미 설정했음
    
    while 1:
        #반복문
        
        if len(word) == ansl:
            return word
        #조건 : 하나의 문자열이 생성되면 문자열 리턴
        
        left = ansl - len(word) - 1
        #지금 시행에서 붙이고 남은 길이
        
        maxB = left // 2 
        #B를 붙일 수 있는 최대 갯수
        
        maxC = left // 3 
        #C를 붙일 수 있는 최대 갯수
        #최대 갯수를 알면 내가 탐색중인 알파벳이 들어갔을때 유효한지 미리 알 수 있다.
        
        if left % 2 != 0:
            maxB += 1
        if left % 3 != 0:
            maxC += 1
        #최대 갯수 구체화
        
        if cntList[2] > 0 and cntList[1] <= maxB and dis[2] >= 2:
        #c의 갯수가 존재하고, b의 갯수가 b의 최댓수를 안넘고, c의 조건이 맞을때
            word += 'C'
            cntList[2] -= 1
            dis[0] += 1
            dis[1] += 1
            dis[2] = 0
            continue
        
        #a,b,c 거리 갱신/c갯수 갱신/word 갱신
        if cntList[1] > 0 and cntList[2] <= maxC and dis[1] >= 1:
        #b의 갯수가 존재하고, c의 갯수가 c의 최댓수를 안넘고, b의 조건이 맞을때
            word += 'B'
            cntList[1] -= 1
            dis[0] += 1
            dis[1] = 0
            dis[2] += 1
            continue
        #갱신
        
        if cntList[0] > 0:
        #a의 갯수가 존재할때
            word += 'A'
            cntList[0] -= 1
            dis[0] = 0
            dis[1] += 1
            dis[2] += 1
            continue
        #갱신
        
        break
    
    return -1
    #아무것도 없을때 -1 리턴
    
if __name__ == '__main__':

    main()