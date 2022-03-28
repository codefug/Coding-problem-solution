#2609 최대공약수와 최소공배수

n1,n2=map(int,input().split())

max_n1=n1
max_n2=n2

while max_n1%max_n2!=0:

    res=max_n1%max_n2

    max_n1=max_n2

    max_n2=res

print(max_n2)

min_n1=n1
min_n2=n2

while min_n1!=min_n2:

    if min_n1>min_n2:

        min_n2+=n2

    else:

        min_n1+=n1

print(min_n1)
