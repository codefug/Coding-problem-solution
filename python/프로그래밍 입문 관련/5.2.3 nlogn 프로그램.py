def quicksort(n):
    if len(n)>=1:
        low=1
        high=len(n)-1
        a=n[0]
        list1,list2=[],[]
        while n[low]<=a:
            while n[high]>=a:
                high-=1
                if high==0:
                    for i in range(1,len(n)):
                        list2.append(n[1])
                    break
            if high==0:
                    break
            if low==len(n):
                n.remove(a)
                n.append(a)
                for i in range(0,len(n)-1):
                    list1.append(n[i])
                break
            elif low>=high:
                a,n[high]=n[high],a
                for i in range(0,high):
                    list1.append(n[i])
                for j in range(high+1,len(n)):
                    list2.append(n[j])
                break
            n[low],n[high]=n[high],n[low]
            low+=1
            print(list1,list2)
        return quicksort(list1),quicksort(list2)
    else:
        return n
