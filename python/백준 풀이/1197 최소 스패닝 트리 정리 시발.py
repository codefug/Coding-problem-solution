#1197 최소 스패닝 트리 정리
from sys import stdin

input=stdin.readline

def get_parents(parents,a):

    if parents[a]==a:

        return a

    parents[a]=get_parents(parents,parents[a])

    return parents[a]

def union_parents(arr,a,b):

    a=get_parents(arr,a)

    b=get_parents(arr,b)

    if a>b:

        arr[a]=b

    else:

        arr[b]=a
def kruskal():

    edges=0

    answer=0

    parents=[i for i in range(v+1)]

    graph.sort(key=lambda x:x[2])

    for start,end,cost in graph:
        if get_parents(parents,start)!=get_parents(parents,end):

            edges+=1

            union_parents(parents,start,end)

            answer+=cost

        if edges==v-1:

            break

    return answer
v,e=map(int,input().split())

graph=[list(map(int,input().split())) for i in range(e)]

print(kruskal())
