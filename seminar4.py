# Задача1
# Вычислить число c заданной точностью *d*
import math

p = math.pi
d = float(input('Введите число d = '))
count = 0
if d == 0:
    print('Введите значение d в пределах от 0.1 до 0.0000000001!')
while d < 1:
    count += 1
    d = d*10
print(f'Число {p} с заданной точностью d = ', (round(p, count)))  


# Задача2
#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input('Введите натуральное число N  = '))
list = []
num = N
n = 2
while n <= N:
    while N % n == 0:
        list.append(n)
        N = N / n
    n = n + 1
if N > 1:
    list.append(N)
print(f'Простые множители числа {num} можно увидеть в списке: {list}')


# Задача3 
#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности.
from random import randint
def createlist(n):
    list = []
    for i in range(n):
        list.append(randint(0, 10))
    return list
m = int(input("Введите количество элементов: "))
mylist = createlist(m)
print(mylist)
new_list = []
for i in range(len(mylist)):
    if mylist.count(mylist[i]) == 1:
        new_list.append(mylist[i])
print(new_list)


# Задача4
#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
#многочлена и записать в файл многочлен степени k
from random import randint

k = int(input('Введите коэффициент k = '))

def writefile(m):
    with open ('file.txt', 'w') as data:
        data.write(m)

def create_list(n):
    list = []
    for i in range(n + 1):
        list.append(randint(0,100))
    return list

def create_str(l):
    list = l[::-1]
    num = ' '
    if len(list) < 1:
        num = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                num += f'{list[i]}x^{list[i] - 1}'
                if list [i +1] != 0:
                    num += '+'
            elif i == len(list) - 2 and list[i] != 0:
                num += f'{list[i]}x'
                if list[i + 1] != 0:
                    num += '+'
            elif i == len(list) - 1 and list[i] != 0:
                num += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                num += ' = 0'
    return num
list = create_list(k)
writefile(create_str(list))
print(list)
Я здесь запуталась( и не смогла додумать

from random import randint
max_val=100
k = int(input('Введите коэффициент k:'))
koef=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koef) if j][::-1])
poly=poly.replace('x^1+', 'x+')
poly=poly.replace('x^0', '')
poly+=('','1')[poly[-1]=='+']
poly=(poly, poly[:-2])[poly[-2:]=='^1']
print(poly)

# Задача5
#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.
file1 = 'file1.txt'
file2 = 'file2.txt'
file_sum = 'filesum.txt'

def read_pol(file):
    with open(str(file), 'r') as data:
        poly = data.read()
    return poly

def addpoly(p1,p2):
    i=0
    su=0
    j=0
    c=[]
    if len(p1)==0:
        return p2
    if len(p2)==0:
        return p1
    while i<len(p1) and j<len(p2):
        if int(p1[i][1])==int(p2[j][1]):
            su=p1[i][0]+p2[j][0]
            if su !=0:
                c.append((su,p1[i][1]))
            i=i+1
            j=j+1
        elif p1[i][1]>p2[j][1]:
            c.append((p1[i]))
            i=i+1
        elif p1[i][1]<p2[j][1]:
            c.append((p2[j]))
            j=j+1
    if p1[i:]!=[]:
        for k in p1[i:]:
            c.append(k)
    if p2[j:]!=[]:
        for k in p2[j:]:
            c.append(k)
    return c

def write_to_file(file, poly):
    with open(file, 'w') as data:
        data.write(poly)

