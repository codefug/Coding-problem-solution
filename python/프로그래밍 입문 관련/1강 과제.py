a=int(input("a="))
x=int(input("x="))
e=int(input("e="))
n=1
d=0
while e<0:
    print("e는 음이 아닌 정수입니다.")
    e=int(input("e="))
if e!=0:
   while n==e:
       x=x*e
       n+=1
d=a*x
if e==0:
    d=1
print(d)
