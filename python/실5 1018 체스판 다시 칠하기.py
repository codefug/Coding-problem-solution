#1018 체스판 다시 칠하기

n,m=map(int,input().split())

board=[input() for i in range(n)]

white=""
black=""

for i in range(8):
    
    if i%2==1:
        white+="B"
        black+="W"
    
    else:
        white+="W"
        black+="B"
        
def chess_board(y,x):
    chess=[]
    for i in range(8):
        chess.append(board[y+i][x:x+8])
    return chess

def mini(chess):
    ans_w=0
    ans_b=0
    
    for i in range(8):
    
        for j in range(8):
            if i%2==0:
                if white[j]==chess[i][j]:
                    ans_b+=1
                if black[j]==chess[i][j]:
                    ans_w+=1
            if i%2==1:
                if white[j]==chess[i][j]:
                    ans_w+=1
                if black[j]==chess[i][j]:
                    ans_b+=1
    return min(ans_w,ans_b)

'''
함수2 시작점 xy에 최솟값 저장
1. 검 시작
2. 흰 시작
'''
min_ans=81
for i in range(n-7):
    for j in range(m-7):
        chess=chess_board(i,j)
        min_ans=min(min_ans,mini(chess))
        
print(min_ans)
             
'''
n-7 m-7로 함수1 돌리고
찾은 체스판으로 함수2 돌림
dp에서 가장 작은 값 출력
'''