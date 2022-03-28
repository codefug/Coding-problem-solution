from sys import stdin,exit
input=stdin.readline
def find(l,x):
    if l.count(x)==0:
        return -1
    else:
        return l.index(x)
n,k=map(int,input().split())
l=list(input().split())
if n>=k:
    print(0)
    exit(0)
count=0
'''
기본 이념
기계에 0~n개까지 넣고 다음부터는 con이 l에서 제일 마지막에 나오는 index를 가진
기계에 투입 count+1 이걸 반복.(만약 기계에 이미 있다면 count를 올리지 않음)
'''
con=[]
for i in range(n):
    con.append(l[i])
for i in range(n,k):
    if l[i]!=con:
        for j in con:
            result=find(l,j)
            max_result=max(max_result,result)
print(count)
        
        
