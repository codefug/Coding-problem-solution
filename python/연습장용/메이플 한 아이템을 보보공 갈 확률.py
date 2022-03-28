import random
def bobogong(n):
    k=0
    s=0
    for i in range(n):
        a=random.randint(1,1000000)
        b=random.randint(1,1000000)
        c=random.randint(1,1000000)
        d=random.randint(1,1000000)
        e=random.randint(1,1000000)
        f=random.randint(1,1000000)
        if k==0 and a<=47619:
            k+=1
        if k==1 and b<=19608:
            k+=1
        if k==2 and c<=4975:
            k+=1
        if k==3 and d<=25000:
            k+=1
        if k==4 and e<=124:
            k+=1
        if k==5 and f<=249:
            k+=1
        if k==6:
            s+=1
            k=0
    return s


    


n=int(input("n="))
print(f"레어아이템을 {n}번 돌리면 보보공 나오는 횟수는?",bobogong(n))
print(f"드는 비용은 {n*4900}원")
