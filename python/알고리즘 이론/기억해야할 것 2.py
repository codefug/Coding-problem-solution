import random
def makerun(n):
    i=0
    m=1
    j=i
    while i<len(n):
        t=[]
        t.append(str(n[j]))
        i+=1
        j=i
        while j<len(n) and n[j]>n[j-1]:
            t.append(str(n[j]))
            j+=1
        i=j
        print(f"run{m} :"," ".join(t))
        m+=1
        
        


n=int(input("리스트의 원소 개수 입력:"))
line=[]
for i in range(n):
    r=random.randint(1,n)
    line.append(r)
print(line)
makerun(line)
