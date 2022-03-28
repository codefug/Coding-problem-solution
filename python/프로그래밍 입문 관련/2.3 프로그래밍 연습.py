def makeList(x):
    s=[]
    x=x.split( )
    return x

fin=open('input.txt','r')
line=fin.readline()
s=makeList(line)
print(s)
