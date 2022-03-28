#2252 줄 세우기
from collections import defaultdict

from sys import stdin

input=stdin.readline

n,m=map(int,input().split())

number=defaultdict(list)

visited=[False] * (n+1)

for i in range(m):

    a,b=map(int,input().split())

    number[a].append(b)

stack=[]

def topologicalSortUtil(v,visited,stack):

    visited[v]=True

    if number[v]:

        for i in number[v]:

            if visited[i]==False:

                topologicalSortUtil(i,visited,stack)

    stack.append(v)

def topologicalSort():

    for i in range(1,n+1):

        if visited[i]==False:

            topologicalSortUtil(i,visited,stack)

for i in range(1,n+1):

    if visited[i]==False:

        topologicalSort()

stack.reverse()

print(''.join(map(str,stack)))
