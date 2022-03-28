n=int(input())
x,y=input().split()
for i in range(n):
    m[i]=int(m[i])
sero=[]
for i in range(19):
    garo=[]
    for j in range(19):
        garo.append(0)
    sero.append(garo)

for i in range(19):
    for j in range(19):
        if j==x-1 and i==y-1:
            print(i,end=' ')
        else:
            print(0,end=' ')
        
