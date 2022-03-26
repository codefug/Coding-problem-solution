#2439 별 찍기-2

from os import sep


n=int(input())

for i in range(1,n+1):
    
    for j in range(n):
        
        if i+j<n:
            
            print(" ",end="")
        else:
            print("*",end="")
        
    print( )