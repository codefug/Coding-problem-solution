#1085

x,y,w,h=map(int,input().split())

x_gap=min(w-x,x)

y_gap=min(h-y,y)

print(min(x_gap,y_gap))