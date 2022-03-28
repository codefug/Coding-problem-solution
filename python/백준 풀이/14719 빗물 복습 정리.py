#14719 빗물

'''
#시간 오래걸려도 하나씩 생각해보는 정리
h,w=map(int,input().split())

block=list(map(int,input().split()))

result=0

for i in range(1,w-1):

    result+=max(0,(min(max(block[:i]),max(block[i+1:]))-block[i]))

print(result)
'''
#처음의 내 생각을 구현해놓은 시간 오래걸리지 않지만 힘든 구현
h,w=map(int,input().split())

block=list(map(int,input().split()))

the longgest=max(block)

result=(the longgest*w) -sum(block)

for i in range(w):

    if block[i]==the longgest:
        
        l=i
        
        break
    
for j in range(w-1,-1,-1):

    if block[j]==the longgest:

        r=j

        break

l_max=the longgest

r_max=the longgest

while l>0:

    l_sub_max=max(block[:l])

    for i in range(l-1,-1,-1):

        if block[i]==l_sub_max:

            index=i

            break

    result= 
