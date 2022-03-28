def foranswer(d,i,yonsan,l):
    for j in range(i,len(yonsan)-1):
        yonsan[i],yonsan[j+1]=yonsan[j+1],yonsan[i]
        foranswer(d,i+1,yonsan,l)
        yonsan[i],yonsan[j+1]=yonsan[j+1],yonsan[i]
    k=int(d[0])
    for a in range(1,len(d)):
        d[a]=int(d[a])
        if yonsan[a-1]==0:
            k=k+d[a]
        if yonsan[a-1]==1:
            k=k-d[a]
        if yonsan[a-1]==2:
            k=k*d[a]
        if yonsan[a-1]==3:
            k=k//d[a]
    l.append(k)

N=int(input())
d=list(input().split())
y=list(input().split())
yonsan=[]
print(y)
for i in range(len(y)):
    for j in range(int(y[i])):
        yonsan.append(i)
l=[]
foranswer(d,0,yonsan,l)
print(max(l))
print(min(l))
