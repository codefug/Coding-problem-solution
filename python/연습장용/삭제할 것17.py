d=[]
t=0
for i in range(9):
    k=int(input())
    t+=k
    d.append(k)
print(d)
for i in range(9):
    for j in range(9):
        if t-(d[i]+d[j])==100:
            T=d
            print(d)
            print(T)
            T.remove(d[i])
            T.remove(d[j])
            print(d)
            print(T)
for i in range(len(T)):
    print(T[i])
