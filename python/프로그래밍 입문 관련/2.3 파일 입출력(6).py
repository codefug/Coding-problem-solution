fout=open('output.txt','w')
for c in range(0,51,10):
    f=int(c*9/5+32)
    out='섭씨 온도:%d,화씨 온도:%d\n'%(c,f)
    fout.write(out)
fout.close()
