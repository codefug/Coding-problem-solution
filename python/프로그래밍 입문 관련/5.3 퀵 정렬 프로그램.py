#퀵 정렬
import random, time
def quick1sort(n):
    if len(n)<=1:
        return n
    else:
        a=n[0]
        print("a",a)
        right,left=[],[]
        for i in range(1,len(n)):
            if a<n[i]:
                right.append(n[i])
            else:
                left.append(n[i])
        return quick1sort(left)+[a]+quick1sort(right)


for i in range(100):
    n=[]
    for i in range(7):
        n.append(random.randint(1,8))

    print(n)
    print(quick1sort(n))

