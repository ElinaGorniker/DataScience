# для начала импортируем модули, которые понадобятся нам для написание классификатора
# numpy - библиотека для работы с массивами(матрицами в том числе), помогает делать различные операции над ними
import numpy as np
from matplotlib import pyplot as plt

import seaborn as sns

# с помощью этой команды графики будут отображаться в текущем окне в ноутбуке под ячейкой, где написан код для отображения графика


# Зафиксируем случайность, чтобы каждый раз получалось одно и тоже
np.random.seed(seed=42)


p1 = np.random.normal(loc=0, scale=1, size=(50,2))
p2 = np.random.normal(loc=5, scale=2, size=(50,2))
p3 = np.random.normal(loc=10, scale=0.8, size=(50,2)) - np.array([5, -5])


X = np.concatenate((p1, p2, p3))
y = np.array([1]*50 + [2]*50 + [3]*50)

point = [2, 2.5]

plt.scatter(p1[:,0], p1[:, 1], color='blue')
plt.scatter(p2[:,0], p2[:, 1], color='orange')
plt.scatter(p3[:,0], p3[:, 1], color='green')
plt.scatter(point[0], point[1], s = 100, color='red')


def euclidian_metric(a, b):
    return np.sqrt(np.sum(np.power(a - b, 2)))

# запустим эту ячейку, чтобы проверить, всё ли верно реализовано на текущем этапе
# если возникает ошибка в assert, то при реализации функций была допущена ошибка
# если появляется текст из print - на данном этапе ошибок нет
a = np.zeros((1,4))
b = np.ones((1,4))

assert euclidian_metric(a,b)[0] == 2
print('ошибок нет')