#1920 수 찾기

n=int(input())

<<<<<<< Updated upstream
n_l=sorted(list(map(int,input().split())))
=======
<<<<<<< HEAD
n_l=list(map(int,input().split()))
=======
n_l=sorted(list(map(int,input().split())))
>>>>>>> ab24d36f4dce779af2f8b30467dabc7f075d6973
>>>>>>> Stashed changes

m=int(input())

m_l=list(map(int,input().split()))

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
n_l.sort()

m_l.sort()

start=0
end=len(m_l)

=======
>>>>>>> Stashed changes
def two(l,start,end):
    
    if start>end:
        
        return 0
    
    mid=(start+end)//2
    
    if n_l[mid]==l:
        
        return 1
    
    if n_l[mid]>l:
        
        return two(l,start,mid-1)
        
    else:
        
        return two(l,mid+1,end)
    
for i in m_l:
<<<<<<< Updated upstream
    print(two(i,0,len(n_l)-1))
=======
    print(two(i,0,len(n_l)-1))
>>>>>>> ab24d36f4dce779af2f8b30467dabc7f075d6973
>>>>>>> Stashed changes
