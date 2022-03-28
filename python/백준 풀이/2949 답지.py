R,I=range,input
h,w=map(int,I().split())
b=eval('I(),'*h)
n=int(I())
exec(n//90*'*b,=zip(*b[::-1]);h,w=w,h;')
n%90and[print(' '*abs(h+~i)+' '.join(b[i-c][c]for c in R(w)if 0<=i-c<h))for i in R(h+w-1)]or[print(*z,sep='')for z in b]
