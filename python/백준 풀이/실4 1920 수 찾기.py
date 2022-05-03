#1920 수 찾기

n=int(input())

n_l=sorted(list(map(int,input().split())))

m=int(input())

m_l=list(map(int,input().split()))

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
    print(two(i,0,len(n_l)-1))