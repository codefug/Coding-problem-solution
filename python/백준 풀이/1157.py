n=input()
n=n.upper()
m=set(n)

l=dict({})

for i in m:
    l[i]=n.count(i)

a=max(l.values())
b=''

for j in l:
    if l.get(j)==a:
        b+=j

if len(b)!=1:
    print('?')
else:
    print(b)
    
