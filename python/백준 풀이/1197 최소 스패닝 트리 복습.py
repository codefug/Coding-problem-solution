#1197 최소 스패닝 트리 복습

def get_parents(arr,a):

    if arr[a]==a:

        return a

    arr[a]=get_parents(arr,arr[a])

    return arr[a]

def find_parents(arr,a,b):

    a=get_parents(arr,a)
    
    b=get_parents(arr,b)

    return a==b

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

    order.sort(key=lambda x:x[2])

    parents=[i for i in range(v+1)]

    for start,end,cost in order:
    
        if not find_parents(parents,start,end):

            union_parents(parents,start,end)

            answer+=cost

            edges+=1
        
        if edges==v-1:

            break

    return answer
        
v,e=map(int,input().split())

order=[list(map(int,input().split())) for i in range(e)]

print(kruskal())
