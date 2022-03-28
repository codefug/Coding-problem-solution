d=[]
t=0
for i in range(9):
    k=int(input())
    t+=k
    d.append(k)
for i in range(8):
    for j in range(i+1,9):
        if t-(d[i]+d[j])==100:
            T=list(d)
            T.remove(d[i])
            T.remove(d[j])
for i in range(len(T)):
    print(T[i])
