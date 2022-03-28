def sum_avg(x, y, z):
    a=x+y+z
    b=(x+y+z)/3
    return (a,b)

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
a,b=sum_avg(a,b,c)
print("합:",a)
print("평균:",b)





