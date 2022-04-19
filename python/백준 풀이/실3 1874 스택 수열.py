#1874 스택 수열

n=int(input())

l=[]

for i in range(n):
    
    l.append(int(input()))

num_l=[i for i in range(2,n+1)]

stack=[1]

while stack:
    
    #stack에 맨 뒤에 값이 l[현재값]보다 작으면 stack에 더 넣고
    #