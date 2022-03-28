def stringsearch(a,i,n):
    for q in range(i):
        if a[q]==n[0]:
            for p in range(len(n)):
                if n[p]!=a[q+p]:
                    break
            if p==len(n)-1:
                return q
    return False








fin=open('input.txt','r')
line=fin.readline()
n=len(line)
line2=input("패턴 입력:")
if stringsearch(line,n,line2):
    print(stringsearch(line,n,line2))
else:
    print("그런건 없다")
