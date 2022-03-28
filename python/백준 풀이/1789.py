s=int(input())
n=0
i=1
while s>0:
    s-=i
    if s>0:
        break
    else:
        i+=1
        n+=1
print(n)
