# for start print in the console: python3 App.py

# Python-пакеты для курса
# pip3 install numpy scipy pandas scikit-learn
# http://www.numpy.org/ NumPy: работа с массивами и матрицами (the fundamental package for scientific computing)
# http://pandas.pydata.org/ Pandas: обработка наборов данных (data structures and data analysis tools)
# https://matplotlib.org/ Matplotlib: визуализация данных (plotting library)
# http://scikit-learn.org/stable/ SciKit-Learn: библиотека алгоритмов машинного обучения (tools for data mining)
# https://www.scipy.org/ SciPy: вспомогательные функции (open-source software for mathematics, science, and engineering)

import numpy as np

# матрица, состоящая из 1000 строк и 50 столбцов
# loc: среднее нормального распределения (в нашем случае 1)
# scale: стандартное отклонение нормального распределения (в нашем случае 10)
# size: размер матрицы (в нашем случае (1000, 50))
matrix = np.random.normal(loc=1, scale=10, size=(1000, 50))
# print(m)

# Нормировка матрицы
m = np.mean(matrix, axis=0)
std = np.std(matrix, axis=0)
X_norm = ((matrix - m) / std )

# print(X_norm)

# Операции над элементами матрицы
Z = np.array([[4, 5, 0],
             [1, 9, 3],
             [5, 1, 1],
             [3, 3, 3],
             [9, 9, 9],
             [4, 7, 1]])


n = 0
for row in Z:
    items_count = 0
    for item in row:
        items_count = items_count + item
    if items_count > 10:
        print(n)
    n = n + 1

r = np.sum(Z, axis=1)
# print(np.nonzero(r > 10))
# print(r)

# Объединение матриц
X = np.eye(3)
Y = np.eye(3)
Z = np.vstack((X, Y))
print(Z)