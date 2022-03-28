import sys

sys.setrecursionlimit(10**6)
#재귀 한계 늘리기
input=sys.stdin.readline
#스탠다드 인풋
n,m,v=map(int,input().split())
#정점 간선 첫 정점번호 입력
order=[[] for i in range(n+1)]
#순서를 넣을 리스트 작성
for i in range(m):

    a,b=map(int,input().split())

    order[a].append(b)

    order[b].append(a)

[i.sort() for i in order]

dfs_answer=[]

bfs_answer=[]

visited=[False]*(n+1)

def dfs(v):

    visited[v]=True

    dfs_answer.append(v)

    for i in order[v]:

        if visited[i]==False:

            dfs(i)

dfs(v)

print(*dfs_answer)

def bfs(v):

    que=[v]

    while que:

        now=que.pop(0)

        visited[now]=True

        bfs_answer.append(now)

        for i in order[now]:

            if visited[i]==False:

                que.append(i)

                visited[i]=True

visited=[False]*(n+1)

bfs(v)

print(*bfs_answer)
