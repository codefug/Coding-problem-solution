'''
def quicksort(n):
    if len(n)<=1:
        return n
    else:
        a=n[0]
        right,left=[],[]
        for i in range(1,len(n)):
            if a<n[i]:
                right.append(n[i])
            else:
                left.append(n[i])
        return quicksort(left)+[a]+quicksort(right)
'''
#인덱스 값을 받아서 a에 직접 입력시키는 함수
def quicksort(n,l,r):
    if l<r:
        k=n[r]
        i=l-1
        j=r
        while True:
            i+=1
            while k>n[i]:
                i+=1
            j-=1
            while k<n[j]:
                j-=1
            if i>=j:break
            n[i],n[j]=n[j],n[i]
        n[i],n[r]=n[r],n[i]
        quicksort(n,l,i-1)
        quicksort(n,i+1,r)

s=[3,2,4,5,1]
quicksort(s,0,4)
print(s)
