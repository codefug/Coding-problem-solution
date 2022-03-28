def gcd(m, n):
    if m<n:
        m,n=n,m
    while m%n!=0:
        r=m%n
        m=n
        n=r
    return n

a = int(input('a = '))
b = int(input('b = '))
print('최대공약수 : ', gcd(a, b))
