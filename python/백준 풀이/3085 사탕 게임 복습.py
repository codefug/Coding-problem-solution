#3085 사탕 게임 정리

def find_max1(y): #가로줄 세기

    global answer,board,result

    answer=1

    for i in range(1,n):

        if board[y][i]==board[y][i-1]:

            answer+=1

        else:
            
            result=max(result,answer)

            answer=1

    result=max(result,answer)

def find_max2(x): #세로줄 세기

    global answer,board,result

    answer=1

    for i in range(1,n):

        if board[i-1][x]==board[i][x]:

            answer+=1

        else:

            result=max(result,answer)

            answer=1

    result=max(result,answer)

def candy_game(n):

    global result,board

    result=0

    board=[list(*input().split()) for i in range(n)]

    for i in range(n):

        for j in range(1,n):

            board[j][i],board[j-1][i]=board[j-1][i],board[j][i]

            #세로1차이 나는거 끼리 바꿈

            find_max1(j)

            find_max1(j-1)

            find_max2(i)

            board[j][i],board[j-1][i]=board[j-1][i],board[j][i]

            board[i][j],board[i][j-1]=board[i][j-1],board[i][j]

            #가로 1차이 나는거 끼리 바꿈

            find_max1(i)

            find_max2(j)

            find_max2(j-1)

            board[i][j],board[i][j-1]=board[i][j-1],board[i][j]

    return result
    
if __name__=="__main__":

    n=int(input())

    print(candy_game(n))

