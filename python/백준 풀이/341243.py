a=list(range(1,11))
print(a)
for i in a:
    if i==8:
        break
    if i%2==0:
        continue
    print(i,end='')
print()
print(i)
