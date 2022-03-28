def add(a, b):
    global c
    c = a + b

a = int(input('정수 입력 : '))
b = int(input('정수 입력 : '))
c = 0
add(a, b)
print('c = ', c)
