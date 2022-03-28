#3085 사탕 게임 복습

def candy(board):

    global result

    result=0

    result=max(get_max_number(board,y,x) for y in range(n) for x in range(n))

    dx=[0,0,-1,1]

    dy=[1,-1,0,0]

    for y in range(n):

        for x in range(n):

            for i in range(4):

                nx=x+dx[i]

                ny=y+dy[i]

                if 0<=nx<n and 0<=ny<n:

                    board[y][x],board[ny][nx]=board[ny][nx],board[y][x]

                    get_max_number(board,y,x)

                    board[y][x],board[ny][nx]=board[ny][nx],board[y][x]

    return result

def get_max_number(board,y,x):

    global result

    colar=board[y][x]

    answer1=1

    nx=x-1

    while nx>=0 and board[y][nx]==colar:

        answer1+=1

        nx-=1

    nx=x+1

    while nx<n and board[y][nx]==colar:

        answer1+=1

        nx+=1

    answer2=1

    ny=y-1

    while ny>=0 and board[ny][x]==colar:

        answer2+=1

        ny-=1

    ny=y+1

    while ny<n and board[ny][x]==colar:

        answer2+=1

        ny+=1

    result=max(answer1,answer2,result)

    return result

n=int(input())

board=[[i for i in input()] for i in range(n)]

print(candy(board))
