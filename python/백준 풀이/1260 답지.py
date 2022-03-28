import sys

sys.setrecursionlimit(10**6)

def dfs(current):
    
    visited[current] = True
    
    dfs_list.append(current)
    
    for node in adj[current]:
        
        if not visited[node]:
            
            dfs(node)
        
def bfs(root):
    
    visited[root] = True

    que = []

    que.append(root)

    while que:

        current = que.pop(0)

        bfs_list.append(current)

        for node in adj[current]:

            if not visited[node]:

                que.append(node)

                visited[node] = True

N, M, V = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

[node.sort() for node in adj]
    
dfs_list = []
bfs_list = []
                
visited = [False] * (N + 1)                
dfs(V)
print(*dfs_list)
visited = [False] * (N + 1)
bfs(V)
print(*bfs_list)
