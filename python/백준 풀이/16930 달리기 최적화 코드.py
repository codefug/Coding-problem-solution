import sys
sys.setrecursionlimit(10000000)
#반복 제한 해제

def getInput():
    
    return sys.stdin.readline().strip()
#빠른 입력

X, Y, K = map(int, getInput().split())
board = [getInput() for j in range(X)]
i, j, x, y = map(int, getInput().split())
i-=1
j-=1
x-=1
y-=1
#입력 각 시작점 끝점은 인덱스화

curNodes = [[(i,j)], [(x,y)]]
#큐 curNodes

ds = [(1, 0),(-1, 0),(0, 1),(0, -1)]
#4방향

count = [0, 0]
#인덱스 0 은 시작점부터 생각한 시간 초 1은 끝점부터 생각한 시간 초

index = 0
#0일때는 시작점부터 시작 1일때는 끝점부터 시작

done = [[[0 for i in range(Y)] for j in range(X)] for k in range(2)]
#2배로 만든 visited 리스트

isAnswer = False
#flag

answer = float('inf')
#지금 답은 최대값으로

while curNodes[index]:
#큐를 돌려서
    nextNodes = []
#nextNodes 갱신
    
    for i, j in curNodes[index]:
#큐 안에 있는 x y 꺼냄
        
        if done[index^1][i][j]:
            isAnswer = True
            answer = min(answer, done[index][i][j]+done[index^1][i][j])
#만약 done[index의 반대값][x][y]가 있다면 flag True 로 하고 답 갱신하는데
#done의 모든 값을 더한거랑 비교

        for dx, dy in ds:
#4방향
            
            for k in range(1, K+1):
#k 1부터 돌림
                
                x, y = i+dx*k, j+dy*k
#관계식
                
                if not (0 <= x < X and 0 <= y < Y) or board[x][y] == "#": break
#조건 안맞으면 컷
                
                elif done[index][x][y] != 0 and done[index][x][y] <= count[index]: break
#탐색 됐고 count가 지금보다 크면 break
                
                elif done[index][x][y] != 0: continue
#탐색 됐고 count가 지금보다 작으면 continue

                nextNodes.append((x,y))
                done[index][x][y] = count[index] + 1
#nextNodes에 저장 done[index][x][y]를 count +1 로 바꿈

    if isAnswer:
        print(answer)
        exit()
#print하고 exit 함
        
    curNodes[index] = nextNodes
#curNodes[index] 를 다음 노드 로 갱신
    
    if len(curNodes[index]) == 0:
        break
#nextNodes 가 없다면 break
    
    count[index] += 1
#count[index] 1 더해줌
    
    if len(curNodes[0]) < len(curNodes[1]):
        index = 0
    else:
        index = 1
#curNodes[0]보다 curNodes[1]이 더 크면 index=0 아니면 index=1
        
print(-1)
"""
이 index의 정체에 대해서 알면 이해 될듯
ㅇㅋ 이해 갔음
index는 0일때는 시작점부터 시작 1일때는 끝점부터 시작하는 리스트
한방향으로 가면 가지가 너무 많아지니 양쪽에서 가지 친 다음에 만나는 가지 리턴 하는 코드였음
"""
