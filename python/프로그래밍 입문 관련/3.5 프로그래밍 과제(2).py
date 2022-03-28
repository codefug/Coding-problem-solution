import random
n=int(input("리스트의 원소 개수 입력:"))
line=[]

for i in range(n):
    line.append(random.randint(1,100))
r=[]
i=0
m=1
print(line)

while i<len(line):
    r=[]
    r.append(line[i])
    i+=1
    j=i
    while j<len(line) and line[j]>line[j-1]:
        r.append(line[j])
        j+=1
    print('run%d : %s'%(m,r))
    i=j
    m+=1




    

