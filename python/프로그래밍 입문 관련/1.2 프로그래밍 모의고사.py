a=int(input("a="))
b=int(input("b="))
t=1
if a>b:
    a,b=b,a
    
while a<=b:
    t=a*9/5+32
    print("섭씨 :",a,"화씨 :",t)
    a+=5
