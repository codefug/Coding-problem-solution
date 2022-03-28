n=input()

while n!="0":
    flag=0
    for i in range(len(n)//2):
        if n[i]!=n[len(n)-i-1]:
            flag=1
            break
    if flag==0:
        print("yes")
    else:
        print("no")
    n=input()