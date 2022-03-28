#3460 이진수 정리

#1
t=int(input())

for i in range(t):

    n=int(input())

    n=format(n,'b')

    for i in range(-1,-(len(n))-1,-1):

        if n[i]=='1':

            print(-i-1,end=' ')

        
