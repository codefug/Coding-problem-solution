def sum_average(a,b,c):
    sum_int=a+b+c
    average_int=sum_int/3
    return(sum_int,average_int)

a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
result=sum_average(a,b,c)
print('합=%d, 평균=%f'%(result[0],result[1]))
