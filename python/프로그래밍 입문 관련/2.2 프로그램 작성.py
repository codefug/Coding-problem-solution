str1=list(input('평문 입력:'))
k=int(input("k 값 입력(1~26):"))
n=len(str1)
str2=''
for i in range(n):
    if ord(str1[i])+k==123:
        str1[i]=chr(32-k)
    elif ord(str1[i])==32:
        str1[i]=chr(96)
    elif ord(str1[i])+k>123:
        str1[i]=chr(ord(str1[i])-27)

        
    
        
    str2=str2+chr(ord(str1[i])+k)
    print(str2)      

    
print("암호문 출력:",str2)



                                           




