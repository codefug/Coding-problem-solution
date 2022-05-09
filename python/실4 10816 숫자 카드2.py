#10816 숫자 카드2

from sys import stdin

input=stdin.readline

n=int(input())

l=list(map(int,input().split()))

m=int(input())

in_l=list(map(int,input().split()))

answer={}

for i in in_l:
    
    answer[i]=0

for i in in_l:
    
    if i in l:
        
        answer[i]+=1
        
print(' '.join(f"{answer[m]}"for m in in_l))