# -*- coding: utf-8 -*-
"""Assurance of Learning  (AoL).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cCVCSOSW75aQbT_kcY8jW4iFScmXX3rk

Alvi Aulia Fatikha\
2602182865

#No. 1 D
"""

# 1 D
import matplotlib.pyplot as plt

# Data
years = [1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,1990,
         1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
temperatures = [14.1999, 14.2205, 14.2411, 14.13765, 14.0342, 14.1519,
                14.2696, 14.2333, 14.197, 14.25125, 14.3055, 14.2454,
                14.1853, 14.2715, 14.3577, 14.3882, 14.4187, 14.38125, 14.3438]

# Plotting
plt.plot(years, temperatures, marker='o', linestyle='-')
plt.xlabel('Tahun')
plt.ylabel('Temperature (°C)')
plt.title('Relasi Antara Temperature dan Tahun')
plt.grid(True)
plt.show()

"""#No. 2 A"""

# 2 A
import math

def taylor_sin(x):
  result = 0
  for n in range(5):
    result += ((-1)**n) * (x**(2*n+1)) / math.factorial(2*n+1)
  return result

def taylor_cos(x):
  result = 0
  for n in range(5):
    result += ((-1)**n) * (x**(2*n)) / math.factorial(2*n)
  return result

def taylor_sin_cos(x):
  return taylor_sin(x) * taylor_cos(x)

x = float(input('Enter the value of x: '))

sin_approx = taylor_sin(x)
cos_approx = taylor_cos(x)
sin_cos_approx = taylor_sin_cos(x)

print(f"sin(x) = {sin_approx}")
print(f"cos(x) = {cos_approx}")
print(f"sin(x) * cos(x) = {sin_cos_approx}")

"""#No. 2 C"""

# 2 C
import math

def taylor_cos(x, n):
    result = 0
    for i in range(n+1):
        coefficient = (-1)**i
        numerator = x**(2*i)
        denominator = math.factorial(2*i)
        term = coefficient * (numerator / denominator)
        result += term
    return result

phi = math.pi
x = phi / 4
order = 4

# Estimasi cos(π/4) menggunakan deret Taylor order 4
approximation = taylor_cos(x, order)

# Menghitung batas kesalahan pemotongan (truncation error bound)
truncation_error_bound = abs(x**(order + 1) / math.factorial(order + 1))

print("Estimasi cos(π/4):", approximation)
print("Truncation Error Bound:", truncation_error_bound)