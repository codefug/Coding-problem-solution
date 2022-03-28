'''
def quick_sort(n):
    if len(n)==1:
        return [n[0]]
    else:
        a=n[0]
        right,left=[],[]
        for i in range(1,len(n)):
            if n[i]>a:
                right.append(n[i])
            else:
                left.append(n[i])
        return left+[a]+right
n=[3,1,2,4,5]
print(quick_sort(n))
'''
def quick_sort(n,start,end):
    if start<end:
        a=n[start]
        i=start
        j=end+1
        while True:
            i+=1
            print("a값",n[start])
            print("돌기전 i:",i)
            while n[i]<a:
                print("i:",i)
                i+=1
            print("돌기후 i:",i)
            j-=1
            print("돌기전 j:",j)
            while n[j]>a:
                print("j:",j)
                j-=1
            print("돌기후 j:",j)
            if i>=j:
                break
            n[i],n[j]=n[j],n[i]
        n[j],n[start]=n[start],n[j]
        print(n)
        quick_sort(n,start,j-1)
        quick_sort(n,j+1,end)



def quicksort(a,l,r):
    if r>l:
        v=a[r]
        i=l-1
        j=r
        while True:
            i+=1
            print("돌기전 i:",i)
            while a[i] < v:
                i+=1
                print(i)
            print("돌기후 i:",i)
            j-=1
            print("돌기전 j:",j)
            while a[j] > v:
                j-=1
                print(j)
            print("돌기후 j:",j)
            if i>=j:break
            a[i],a[j]=a[j],a[i]
        a[i],a[r]=a[r],a[i]
        print(a)
        quicksort(a,l,i-1)
        quicksort(a,i+1,r)
        
s=[2,6,3,4,6,1]
quicksort(s,0,len(s)-1)
    
    
    
