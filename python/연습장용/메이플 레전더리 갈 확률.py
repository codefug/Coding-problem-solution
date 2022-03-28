import random
def bobogong(n):
    k=0
    for i in range(n):
        a=random.randint(1,1000000)
        b=random.randint(1,1000000)
        c=random.randint(1,1000000)
        d=random.randint(1,1000000)
        e=random.randint(1,1000000)
        f=random.randint(1,1000000)
        if a<=47619 and b<=19608 and c<=4975 and  d<=25000 and e<=124 and f<=249:
            k+=1
    return k


    


n=int(input("n="))
print(f"레어아이템을 {n}번 돌리면 보보공 나오는 횟수는?",bobogong(n))
