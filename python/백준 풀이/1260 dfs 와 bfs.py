#1260 DFS 와 BFS

import sys

sys.setrecursionlimit(10**6)

def dfs(v):

    visited[v]=True

    answer1.append(v)

    for i in order[v]:

        if visited[i]==False:

            dfs(i)    

def bfs(v):

    que=[v]

    while que:

        current=que.pop(0)

        answer2.append(current)

        visited[current]=True

        for i in order[current]:

            if not visited[i]:

                que.append(i)

                visited[i]=True

n,m,v=map(int,input().split())

order=[[] for i in range(n+1)]

for i in range(m):

    a,b=map(int,input().split())

    order[a].append(b)

    order[b].append(a)

[node.sort() for node in order]

visited=[False]*(n+1)

answer1=[]

dfs(v)

visited=[False]*(n+1)

answer2=[]

bfs(v)

print(answer1)

print(answer2)
