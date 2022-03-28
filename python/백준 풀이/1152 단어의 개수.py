#1152 단어의 개수

string=input()

answer=0

flag=0

for order,i in enumerate(string,0):

    if flag==0 and ord(i)==32:

        continue
    
    elif ord(i)==32 or order==len(string)-1:
        
        answer+=1
        flag=0
        print(flag,order,i,answer)

    else:

        flag=1
        
print(answer)
