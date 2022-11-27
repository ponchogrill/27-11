###Array1. Дано целое число N (> 0). Сформировать и вывести целочисленный
###массив размера N, содержащий N первых положительных нечетных чисел:
###1, 3, 5, . . . .
##import random
##n = random.randint(1,10)
##lst = []
##num = 1
##print(n, "чисел в списке")
##for i in range(n):
##    lst.append(num)
##    num = num + 2
##print(lst)
    
##    #Array2. Дано целое число N (> 0). Сформировать и вывести целочисленный
###массив размера N, содержащий степени двойки от первой до N-й: 2, 4,
###8, 16, . . . .
##import random
##n = random.randint(1,10)
##lst = []
##num = 2
##print(n, "чисел в списке")
##for i in range(n):
##    lst.append(num)
##    num = num + num
##print(lst)


###Array3. Дано целое число N (> 1),
###а также первый член A и разность D арифметической прогрессии.
###Сформировать и вывести массив размера N,
###A, A + D, A + 2·D, A + 3·D, . . . .
##import random
##n = random.randint(1,10)
##lst = []
##num = 1
##d = 2
##print(n, "чисел в списке")
##for i in range(n):
##lst.append(num)
##    num = num + d
##print(lst)



###Array4. Дано целое число N (> 1), а также первый член A и знаменатель D
###геометрической прогрессии. Сформировать и вывести массив размера N,
###содержащий N первых членов данной прогрессии:
###A, A·D, A·D2, A·D3, . . . .
##import random
##n = random.randint(1,10)
##lst = []
##num = 2
##d = 3
##print(n, "чисел в списке")
##for i in range(n):
##    lst.append(num)
##    num = num * (d * d) 
##print(lst)


#Array5. Дано целое число N (> 2). Сформировать и вывести целочисленный
#массив размера N, содержащий N первых элементов последовательности
#чисел Фибоначчи FK:
#F1 = 1, F2 = 1, FK = FK−2 + FK−1, K = 3, 4, . . . .
import random
n = random.randint(1,10)
lst = [1,1]
print(n, "чисел в списке")
for i in range(n - 2):
    size = len(lst)
    lst.append(lst[size-1]+lst[size-2])
print(lst)








