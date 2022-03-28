import time
from itertools import combinations

start=time.time()
n, k =map(int, input().split())
l = [input() for _ in range(n)]
alreadyknow = ['a','n','t','i','c']
what = []
wordset = []

if k < 5:
    #a,n,t,i,c,r 을 못가르치면 아예 아무것도 못 읽음
    print(0)
else:

    newl = []
    for i in l:
        if i[:4] != 'anta' or i[len(i)-4:] != 'tica':
            n -= 1
            continue
        i = i[4:]
        i = i[:len(i)-4]
       
        newword = ''   
        for word in i:
           
            if word not in what and word not in alreadyknow:
                what.append(word)

            if word not in newword and word not in alreadyknow:
                newword+=word
        
        wordset.append(newword)    

    if len(what) <= k-5:
        print(n)
    else:
        case = list(combinations(what, k-5))
        mx = 0
        for c in case:
            tmp = 0
            for word in wordset:
                flag = 0
                if word == '':
                    tmp += 1
                else:
                    flag = 0
                    for w in word:
                        if w not in c:
                            flag = 1
                            break
                    if flag == 0:
                        tmp += 1

            mx = max(mx, tmp)
        print(mx)
end=time.time()-start
print(end)


