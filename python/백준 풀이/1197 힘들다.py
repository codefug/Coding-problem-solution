from sys import stdin

input=stdin.readline

v,e=map(int,input().split()) #정점의 개수 v 간선의 개수 e

l=[]

for i in range(e):
    
    a,b,c=map(int,input().split()) #정점 a,b 가중치 c

    l.append([c,a,b])

sorted(l) #오름차순으로 정렬

son=[i for i in range(v+1)]

parent=list.copy(son)

for i in l:
    
    a,b=l[1],l[2]

    
