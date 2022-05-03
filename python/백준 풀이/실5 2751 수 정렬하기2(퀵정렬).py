#실5 2751 수 정렬하기2 퀵정렬

from sys import stdin

input=stdin.readline

n=int(input())
#n입력

l=[int(input()) for i in range(n)]

def quick_sort(start,end,l):

    if start>end:
        return []

    pivot=l[(end-start)//2]
    left=[x for x in l if pivot>x]
    right=[x for x in l if pivot<x]

    if left!=[]:
        left=quick_sort(0,len(left)-1,left)
    if right!=[]:
        right=quick_sort(0,len(right)-1,right)

    return left+[pivot]+right

for i in quick_sort(0,n-1,l):
    
    print(i)