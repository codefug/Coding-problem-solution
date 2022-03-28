#13913 숨바꼭질 4

def f(start,k):

    if start>=k:

        return list(range(start,k-1,-1))

    visited=[False] * (2*k+1)

    visited[start]=True

    curtime=0

    parent={}
    
    todo=[start]

    while todo:

        nexttodo=[]

        curtime+=1

        for n in todo:

            if n > k:

                next=[n-1]

            elif n>=2 and (k/n)%2==0:

                next=[n*2]

            else:

                next=[n-1,n+1,n*2]

            for i in next:

                if i<0 or i>(2*k)+1:

                    continue

                elif i==k:

                    parent[i]=n

                    path=[i]

                    while i!=start:

                        i=parent[i]

                        path.append(i)

                    path.reverse()

                    return path

                elif visited[i]==False:

                    visited[i]=True

                    nexttodo.append(i)

                    parent[i]=n

            print(parent)

        todo=nexttodo
        
    return None

n,k=map(int,input().split())

path=f(n,k)

if path:

    print(len(path)-1)

    print(*path)

else:

    print(-1)
