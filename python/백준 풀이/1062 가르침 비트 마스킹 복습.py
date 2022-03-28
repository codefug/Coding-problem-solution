#1062 가르침 비트 마스킹

from itertools import combinations

n,k=map(int,input().split())

if k<5 or k>=26:

    print(0 if k<5 else n)

else:

    k-=5

    learned={'a','n','t','i','c'}
    
    alpha_list={key:value for value,key in enumerate([set(map(chr,range(ord('a'),ord('z')+1)))-learned])}

    words=[]

    answer=0

    for _ in range(n):
    
        tmp=0

        for c in set(input())-learned:

            tmp|=(1<<alpha_list(c))

        words.append(tmp)

    power2=[2**i for i in range(21)]

    for comb in combinations(power2,k):

        test=sum(comb)

        ct=0

        for word in words:

            if word&test==word:

                ct+=1

        answer=max(answer,ct)

    
