#2309 일곱 난쟁이 정리

l=[int(input()) for i in range(9)]

hap=sum(l)

for i in range(8):

    for j in range(i+1,9):

        if hap-l[i]-l[j]==100:

            a=l[i]

            b=l[j]

            l.remove(a)

            l.remove(b)
                        
            break
        
    if len(l)==7:
        
        break

l.sort()

for i in l:

    print(i)
