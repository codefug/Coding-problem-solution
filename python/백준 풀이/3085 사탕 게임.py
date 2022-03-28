#3085 사탕 게임
def findmax(l):
    n=0
    for i in range(len(l)):
        a=1
        b=1
        for j in range(len(l)):
            if j!=len(l)-1:

                if l[i][j]==l[i][j+1]:

                    a+=1

                    if a>n:
                        n=a
                else:

                    a=1

                if l[j][i]==l[j+1][i]:

                    b+=1

                    if b>n:
                        n=b

                else:

                    b=1                
    return n

def change(l):

    global max_change
    
    for i in range(len(l)):

        for j in range(len(l)):

            if j!=len(l)-1:
                
                l[i][j],l[i][j+1]=l[i][j+1],l[i][j]
                if max_change<findmax(l):
                    max_change=findmax(l)
                l[i][j],l[i][j+1]=l[i][j+1],l[i][j]

            if i!=len(l)-1:
               
                l[i][j],l[i+1][j]=l[i+1][j],l[i][j]
                if max_change<findmax(l):
                    max_change=findmax(l)
                l[i][j],l[i+1][j]=l[i+1][j],l[i][j]
            
n=int(input())

l=[list(input()) for i in range(n)]

max_change=0

change(l)

print(max_change)
