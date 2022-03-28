r,c=map(int,input().split())
li=''
for i in range(r):
    li+=input()
k=int(input())
board=[[0]*10]*10
if k==0:
    for i in range(r):
        for j in range(c):
            print(li[0],end='')
            li=li[1:]
        print()
if k==45:
    l=[]
    for i in range(r+c-1):
        for j in range(r+c-1):
            if i<=r:
                board[i][r]
