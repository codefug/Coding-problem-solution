a=int(input("a="))
t=0
for i in range(1,a):
    if a%i==0:
        t+=1
if t==1:
    print("소수")
else:
    print("안소수")
    
