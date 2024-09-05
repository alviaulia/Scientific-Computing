# -*- coding: utf-8 -*-
"""Assignment2_AlviAuliaFatikha_2602182865.ipynbA

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tF0_DoID6mYTYS6bTN2LztGzlY9POb8A

Alvi Aulia Fatikha\
2602182865

No. 1
"""

# bisection method untuk mencari root dan minimum iteration
import numpy as np
import math

def f(x):
    return 2*x**3 + 7*x - 1

def bisection_method(a, b, tolerance):
    if f(a) * f(b) >= 0:
        print("The function values at 'a' and 'b' do not have opposite signs")
        return None

    while abs(b - a) > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

a = 0.25
b = 1.75
tolerance = 0.0001

root = bisection_method(a, b, tolerance)
if root:
    print("Root found: \n", root)
else:
    print("No root found in the given interval! \n")

def bisection_iterations(a, b, tol):
    return math.ceil(math.log((b - a) / tol) / math.log(2))

# mencari minimum iteration yang dibutuhkan agar tolerance = 0.0000025 jika a = 1 dan b = 2
a = 1
b = 2
tolerance = 0.0000025

iterations = bisection_iterations(a, b, tolerance)
print(f"Minimum number of iterations required: {iterations}")

"""No. 2"""

# newton raphson untuk mencari root dan minimum iteration
import numpy as np

def f(x):
    return 2*x**3 + 7*x - 1

def f_prime(x):
    return 6*x**2 + 7

def newton_raphson_method(f, f_prime, x0, tol, max_iterations):
    x = x0
    num_iterations = 0

    while abs(f(x)) > tol and num_iterations < max_iterations:
        x = x - f(x) / f_prime(x)
        num_iterations += 1

    if abs(f(x)) <= tol:
        return x, num_iterations
    else:
        return None, num_iterations

a = 0.25
b = 1.75
tolerance = 0.0001

root_a, iterations_a = newton_raphson_method(f, f_prime, a, tolerance, max_iterations=1000)
root_b, iterations_b = newton_raphson_method(f, f_prime, b, tolerance, max_iterations=1000)

if root_a is not None:
    print(f"Root found for initial guess (a = {a}) = {root_a}")
    print(f"Minimum number of iterations required guess (a = {a}) = {iterations_a}\n")
else:
    print(f"No root found within the desired tolerance for initial guess a = {a}\n")

if root_b is not None:
    print(f"Root found for initial guess (b = {b}) = {root_b}")
    print(f"Minimum number of iterations required guess (b = {b}) = {iterations_b}\n")
else:
    print(f"No root found within the desired tolerance for initial guess b = {b}\n")

"""No. 3"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
# %matplotlib inline

h = 0.1
x = np.arange(0,2*np.pi, h)
y = np.sin(x)

forward_diff = np.diff(y)/h
x_diff = x[:-1:]
exact_solution = np.cos(x_diff)

plt.figure(figsize = (12, 8))
plt.plot(x_diff, forward_diff, '--', label = 'Finite difference approximation')
plt.plot(x_diff, exact_solution, label = 'Exact solution')
plt.legend()
plt.show()

max_error = max(abs(exact_solution - forward_diff))
print(max_error)