from sys import stdin
input=stdin.readline
v,e=map(int,input().split())
l=[]
parent=[]
for i in range(v+1):
    parent.append(i)
    
for i in range(e):
    a,b,w=map(int,input().split())
    l.append([w,a,b])
    
l.sort()

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    global parent
    root1=find(a)
    root2=find(b)
    if root1>root2:
        parent[root1]=root2
    else:
        parent[root2]=root1
ans=0
while l:
    w,a,b=l.pop(0)
    if find(a)!=find(b):
        union(a,b)
        ans+=w
print(ans)
