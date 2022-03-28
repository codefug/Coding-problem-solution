#3460 이진수 bin 함수 이용한 풀이

#2
t=int(input())
for i in range(t):

    n=int(input())

    n=bin(n)

    for j in range(len(n)-1,1,-1):

        if n[j]=='1':

            print((len(n)-1)-j,end=' ')
