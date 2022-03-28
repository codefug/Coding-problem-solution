def f(x):
    if x<=50:
        x+=1
        f(x+1)
    print(x)

f(3)
