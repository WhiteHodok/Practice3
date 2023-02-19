import numpy as np

#Пункт 1 массив от 0 до 9
print("Пункт 1 , массив чисел от 0 до 9:")
arr = np.arange(10)
print(arr)
print(" ")

#Пункт 2 массив 3 на 3 из Ones
print("Пункт 2 , массив чисел(3х3), состоящий из единиц и f.ones:")
arr = np.ones((3, 3))
print(arr)
print(" ")

#Пункт 3 массив 2х2 с рандомным заполнением
print("Пункт 3 , массив чисел(2х2), состоящий из рандомов:")
arr = np.random.randint(1, 11, size=(2, 2))
print(arr)
print(" ")

#Пункт 4  массив 5х5 от до 1 с rand.int + медиана + вывод
arr = np.random.rand(5, 5)
print("Пункт 4, массив 5х5")
print(arr) # Вывод самого массива
print(" ")
print("Пункт 4, массив 5х5 with mean:")
srednee = np.mean(arr)
print(srednee) # Output медианы
print(" ")

#Пункт 5  массив 5х5 с рандомным заполнением от 0 до 1
print("Пункт 5,  массив 5х5 с рандомным заполнением от 0 до 1:")
arr = np.random.rand(5, 5)
col_sums = arr.sum(axis=0)
print(col_sums)


