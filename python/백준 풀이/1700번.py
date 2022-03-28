from sys import stdin
def grid(idx,left,right,result):
    
    global min_result
    
    if idx==k:
        
        min_result=min(result,min_result)
            
    else:

        if l[idx]!=left and l[idx]!=right:

            grid(idx+1,l[idx],right,result+1)

            grid(idx+1,left,l[idx],result+1)
            
        else:
            
            grid(idx+1,left,right,result)
            
n,k=map(int,input().split())

l=list(map(int,input().split()))

left=l[0]

right=l[1]

min_result=100

grid(2,left,right,0)
