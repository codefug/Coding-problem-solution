from sys import stdin

from collections import defaultdict

input=stdin.readline

n,m=map(int,input().split())

graph=defaultdict(list)

visited=[False]*(n+1)

for i in range(m):

    u,v=map(int,input().split())

    graph[u].append(v)

def topologicalSortUtil(v,visited,stack):

    visited[v]=True

    for i in graph[v]:

        if visited[i]==False:

            topologicalSortUtil(i,visited,stack)

    stack.append(v)

def topologicalSort(v):

    for i in range(1,n+1):

        if visited[i]==False:

            topologicalSortUtil(i,visited,stack)

stack=[]

for i in range(1,n+1):

    if visited[i]==False:

        topologicalSort(i)
        
stack.reverse()
print(' '.join(map(str,stack)))
