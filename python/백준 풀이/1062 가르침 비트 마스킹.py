# 1062 가르침 비트 마스킹

from itertools import combinations

n,k=map(int,input().split())

if k<5 or k>=26:

    print(0 if k<5 else k>=26)

else:

    k-=5

    answer=0

    learned={'a','n','t','c','i'}

    alphabet={key:value for value,key in enumerate(set(map(chr,range(ord('a'),ord('z')+1)))-learned)}

    power2=[2**i for i in range(21)]

    word_list=[]

    for _ in range(n):

        word_to_number=0

        for c in set(input())-learned:

            word_to_number|=(1<<alphabet[c])

        word_list.append(word_to_number)

    for comb in combinations(power2,k):

        test=sum(comb)

        cnt=0

        for word in word_list:

            if test&word==word:

                cnt+=1

        answer=max(cnt,answer)

    print(answer)
