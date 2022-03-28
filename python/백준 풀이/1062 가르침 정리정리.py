#1062 가르침 정리

from sys import stdin

n,k=map(int,input().split())

word_list=[set(input().strip()) for i in range(n)]

alpha=[False for i in range(26)]

if k>=26:

    print(n)

elif k<5:

    print(0)

else:

    k-=5

    
