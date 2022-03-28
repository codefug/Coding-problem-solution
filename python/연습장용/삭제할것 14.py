import random
N = int(input('데이터의 개수 입력 : '))
data = 0
numbers = []
for i in range(N):
    data += random.randint(1, 5)
    numbers.append(data)
print('리스트 : ', numbers)
