h=int(input("높이:"))-1
pascal=[]
pascal.append([1])
for i in range(1,h+1):
    t=[0]*(i+1)
    for j in range(1,i):
        t[j]=(pascal[i-1][j-1]+pascal[i-1][j])
    t[0]=1
    t[i]=1
    pascal.append(t)
for i in pascal:
    print(i)
