def f(x):
    t=[]
    for i in range(x):
        t.append(i)
    return(x,t)

x=5
result=f(x)
print(result[0],result[1])
