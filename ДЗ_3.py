#ДЗ_3
#1) В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из 
#чисел в диапазоне от 2 до 9.

a = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a[j - 2] += 1

i = 0
while i < len(a):
    print(i + 2, '-', a[i])
    i += 1

#2)  Во втором массиве сохранить индексы четных элементов первого массива. 
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо 
#заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), 
#т.к. именно в этих позициях первого массива стоят четные числа.
#done

import random

nums = []
even_nums = []

for i in range(10):
    nums.append(random.randint(1, 100))
    
for n in range(10):
    if nums[n] % 2 == 0:
        even_nums.append(n)

print(nums)
print(even_nums)

#3) В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
#done

import random
a = random.randint(1, 100)
b = random.randint(1, 100)

nums = list(range(a, b))
f = nums[0]
l = nums[-1]
nums[0] = l
nums[-1] = f

print(nums)

#4) Определить, какое число в массиве встречается чаще всего.
#done

from collections import Counter
import random

nums = []
x = 0
while x < 10:
    n = int(input('Введите очередное число:\n'))
    nums.append(str(n))
    x += 1
    
print('\n\n\nВаши числа:', nums)

count = Counter(nums)
count = sorted(list(count.keys()))
print(count[0])

#5) В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
#done

import random

nums = []

for i in range(10):
    nums.append(random.randint(-100, 10))

sort_nums = sorted(nums)
tn = sort_nums[0]

for n in range(10):
    if nums[n] == tn:
        print('Максимальный отрицательный элемент:', tn, '\n', 'Его позиция в массиве:', n)
    else:
        continue

#6) В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.
#done

import random

nums = []

for i in range(10):
    nums.append(random.randint(0, 100))
    
sort_nums = sorted(nums)
min_num = sort_nums[0]
max_num = sort_nums[-1]

for minn in range(10):
    if nums[minn] == min_num:
        break
    else:
        continue

for maxn in range(10):
    if nums[maxn] == max_num:
        break
    else:
        continue

s = []
for n in range(minn + 1, maxn):
    s.append(nums[n])
    
print(nums)
print(sort_nums)
print(sum(s)) #иногда выдает 0, понимаю почему. Одномерный список означает, что минимальный элемент всегда перед
#максимальным? Если да, то мне остается лишь поправить генерацию списка сверху.

#7) В одномерном массиве целых чисел определить два наименьших элемента. 
#Они могут быть как равны между собой (оба являться минимальными), так и различаться.
#done

import random

nums = []

for i in range(10):
    nums.append(random.randint(0, 100))

nums = sorted(nums)

print(nums)
print(nums[0], nums[1]) #Я начинаю подозревать, что функция sorted не одобряется. Увы, я не могу найти 
#другого решения. 
