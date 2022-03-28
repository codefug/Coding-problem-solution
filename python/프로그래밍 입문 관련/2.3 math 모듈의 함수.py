import math

print('x    sinx    cosx    tanx')
print('=========================')
for i in range(0,91,5):
    sinx=math.sin(math.pi*(i/180))
    cosx=math.cos(math.pi*(i/180))
    tanx=math.tan(math.pi*(i/180))
    print("%3d %0.4f %0.4f %0.4f"%(i,sinx,cosx,tanx))
