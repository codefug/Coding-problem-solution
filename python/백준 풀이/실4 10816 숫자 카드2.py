#10816 숫자 카드2

from sys import stdin

input=stdin.readline

n=int(input())

l=list(map(int,input().split()))

m=int(input())

in_l=list(map(int,input().split()))

answer={}

for i in l:
    
    answer[i]=0
    
for i in l:
    
    answer[i]+=1

for i in in_l:
    
    if i in answer:
        
        print(answer[i])
        
    else:
        
        print(0)