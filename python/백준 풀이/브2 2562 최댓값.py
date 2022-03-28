#2562 최댓값

list=[0 for i in range(9)]


for i in range(9):
    
    list[i]=int(input())
    
print(max(list))

print(1+list.index(max(list)))