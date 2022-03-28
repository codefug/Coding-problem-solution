#2252 줄 세우기 정리
from collections import defaultdict

def topologicalSortUtil(index,visited,stack):

    visited[index]=True

    for i in Graph[index]:

        if visited[i]==False:

            topologicalSortUtil(i,visited,stack)

    stack.insert(0,index)

def topologicalSort():

    visited=[False]*(n+1)

    for i in range(m):

        u,v=map(int,input().split())
    
        Graph[u].append(v)

    for i in range(1,n+1):

        if visited[i]==False:

            topologicalSortUtil(i,visited,stack)

    return stack

n,m=map(int,input().split())

stack=[]

Graph=defaultdict(list)

print(*topologicalSort())
