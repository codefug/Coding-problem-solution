n=int(input())
l=[[] for i in range(n)]
for i in range(n):
    l[i]=list(input())
def findmax(l):
    global max_count
    for i in range(len(l)):
        a=1
        b=1
        for j in range(len(l)):
            if j!=len(l)-1:
                if l[i][j]==l[i][j+1]:
                    a+=1
                else:
                    a=1
                if l[j][i]==l[j+1][i]:
                    b+=1
                else:
                    b=1
        if max_count<max(a,b):
            max_count=max(a,b)
max_count=0
for i in range(len(l)):
    for j in range(len(l)):
        if j!=len(l)-1:
            l[i][j],l[i][j+1]=l[i][j+1],l[i][j]
            findmax(l)
            l[i][j],l[i][j+1]=l[i][j+1],l[i][j]
        if j!=len(l)-1:
            l[j][i],l[j+1][i]=l[j+1][i],l[j][i]
            findmax(l)
            l[j][i],l[j+1][i]=l[j+1][i],l[j][i]
print(max_count)
