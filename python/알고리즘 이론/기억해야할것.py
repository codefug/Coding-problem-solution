while i<len(line):
    r=[]
    r.append(str(line[i]))
    i+=1
    j=i
    while j<len(line) and line[j]>line[j-1]:
        r.append(str(line[j]))
        j+=1
    print('run%d : %s'%(m, " ".join(r)))
    i=j
    m+=1






tmp = []
j = 1
for l in line:
    if len(tmp) == 0 or int(tmp[-1]) < l:
        tmp.append(str(l))
    elif int(tmp[-1]) > l:
        print(f"Run_{j}: "," ".join(tmp))
        tmp.clear()
        tmp.append(str(l))
        j += 1
