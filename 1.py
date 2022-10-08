delta = int(input('Введите delta:'))
counter = 0
n = int(input('Введите длину массива: '))
array = []
i = 0
print('Введите массив:')
while i < n:
    array.append(int(input()))
    i+=1
print(array)
minim = array[0]
for i in range(n):
    if array[i] < minim:
        minim = array[i]
print("Минимальный:", minim)
g = minim + delta
f = minim - delta
for i in range(n):
    if array[i] == g or array[i] ==f:
        counter+=1
print('Количество элементов, отличающихся от минимального на дельта:', counter)

