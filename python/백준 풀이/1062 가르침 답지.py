from itertools import combinations

n,k=map(int,input())

if k<5 or k>=26:

    print(0 if k<5 else n)

else:

    k-=5

    learned={'a','n','t','i','c'}

    input_chars=[]

    alpha={ky:v for v,ky in enumerate(set(map(chr,range(ord('a'),ord('z')+1)))-nece_chars)}

    cnt=0

    for _ in range(n):

        tmp=0

        for c in set(input())-learned:

            tmp|=(1<<alpha[c])

        input_chars.append(tmp)

    power_by_2=(2**i for i in range(21))

    for comb in combinations(power_by_2,k):

        test=sum(comb)

        ct=0

        for word in input_chars:

            if test&word==word:

                ct+=1

        cnt=max(cnt,xt)

    print(cnt)
