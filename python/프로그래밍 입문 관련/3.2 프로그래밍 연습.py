import random
def castDice(N):
    a=[0]*6
    for i in range(N):
        r=random.randint(1,6)
        for j in range(1,7):
            if j==r:
                a[j-1]+=1
    for i in range(6):
        print('%0.1f%%'%(a[i-1]/N*100))



N=int(input("N="))
castDice(N)
