#13913 숨바꼭질 4

def f(n,k):

    if n>=k:

        return list(range(n,k-1,-1))

    visited=[False]*(2*k+1)

    visited[n]=True

    todo=[n]

    parent={n:n}

    while todo:

        nexttodo=[]

        for node in todo:

            if node>=k:

                next=[node-1]

            elif node>=1 and (k/node)%2==0:

                next=[node*2]

            else:

                next=[node-1,node+1,node*2]

            for i in next:

                if i<0 or i>2*k:

                    continue

                elif i==k:

                    path=[i]

                    parent[i]=node

                    while i!=n:

                        i=parent[i]

                        path.append(i)

                    return path[::-1]

                elif not visited[i]:

                    visited[i]=True

                    parent[i]=node

                    nexttodo.append(i)

        todo=nexttodo

    return None

n,k=map(int,input().split())

order=f(n,k)

if order:

    print(len(order)-1)

    print(*order)

else:

    print(-1)
