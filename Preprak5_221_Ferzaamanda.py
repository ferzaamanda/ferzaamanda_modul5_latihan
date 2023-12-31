# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HsaF5DUjcLX61G9hYilzQEWNxRBQyZ4F
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, label='Garis')

plt.legend()

plt.show()

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 4, 6, 8, 10, 2, 4, 6, 8, 10])
ypoints = np.array([2, 4, 2, 4, 2, 2, 4, 2, 4, 2])

plt.figure(figsize=(5,5))
plt.plot(xpoints, ypoints, color='black')
plt.xlim([0, 15])
plt.ylim([0, 15])

plt.title('Scatter Plot')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.show()

import matplotlib.pyplot as plt
import numpy as np

Y1 = np.array([1, 3, 5, 7])
Y2 = np.array([2, 4, 6, 8])
Y3 = np.array([3, 5, 7, 9])
Y4 = np.array([7, 5, 3, 1])
Y5 = np.array([8, 6, 4, 2])
Y6 = np.array([9, 7, 5, 3])

plt.plot(Y1, label='Garis 1')
plt.plot(Y2, label='Garis 2')
plt.plot(Y3, label='Garis 3')
plt.plot(Y4, label='Garis 4')
plt.plot(Y5, label='Garis 5')
plt.plot(Y6, label='Garis 6')

plt.title('Plot Banyak Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.legend()
plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]
a = [2, 3, 4, 5, 6]
b = [4, 8, 3, 9, 6]

plt.scatter(a, b, label='Titik 1', color='red')
plt.scatter(x, y, label='Titik 2', color='blue')


plt.title('Scatter Plot')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')


plt.legend()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

sample = np.random.normal(loc=50, scale=5, size=1000)

print(sample)

plt.title('Histogram Sample Data Normal')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi Relatif')
plt.hist(sample, bins=10, density=True)
plt.show()

