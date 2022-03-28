R,I=range,input
h,w=map(int,I().split())
b=eval('I(),'*h)
n=int(I())
exec(n//90*'*b,=zip(*b[::-1]);h,w=w,h;')
