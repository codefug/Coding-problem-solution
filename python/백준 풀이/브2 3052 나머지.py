#3052

ans=0

list=[]
for i in range(10):
    num=int(input())
    if num%42 not in list:
        list.append(num%42)
        ans+=1

print(ans)
