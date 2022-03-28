#2292 벌집

def plussolution(i):
    return sum([n for n in range(i+1)])

n=int(input())

if n==1:

    print(1)

else:
    
    n-=1
    
    if n%6!=0:
        n//=6
        n+=1
    else:
        n//=6

    i=1
    
    while plussolution(i)<n:
        i+=1
    
    print(i+1)