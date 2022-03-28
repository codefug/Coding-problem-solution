h=int(input("높이 h 입력:"))
paskal=[]
paskal.append([1])
for i in range(1,h):
    t=[0]*(i+1)
    for j in range(1,i):
        t[j]=paskal[i-1][j-1]+paskal[i-1][j]
    t[0]=1
    t[i]=1
    paskal.append(t)
for i in paskal:
    for j in i:
        print(j,end='\t')
    print()
k=int(input("행 번호 입력:"))-1
print(paskal[k])
