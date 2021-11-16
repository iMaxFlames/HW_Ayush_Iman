#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:33:29 2021

@author: ayush and iman
"""

# =============================================================================
# Will have to run the cells in order for the code to work properly. 
# Start with this cell.
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

#%% Task 1

def approx_ln(x, n):
    a = (1 + x)/2
    g = np.sqrt(x)
    for i in range(n):
        pre_a = a
        pre_g = g
        a = (pre_a + pre_g)/2
        g = np.sqrt(a*pre_g)
    return (x-1)/a

print(approx_ln(1.41, 5))

#%% Task 2

def f(x):
    return np.log(x)

x_val = np.linspace(1, 10)
y_approx = approx_ln(x_val, 100)
y_true = f(x_val)
plt.plot(x_val, y_approx)
plt.plot(x_val, y_true)
plt.figure()

diff = abs(y_true - y_approx)
plt.plot(x_val, diff)
plt.figure()

#%% Task 3

n_val = list(range(10))
y_approx = [approx_ln(1.41, n) for n in n_val]
y_true = f(1.41)
diff = abs(y_true - y_approx)
plt.plot(n_val, diff)

#%% Task 4

def fast_approx_ln(x, n):
    def d(k, i):
        if k == 0:
            a = (1 + x)/2
            g = np.sqrt(x)
            for n in range(i+1):
                pre_a = a
                pre_g = g
                a = (pre_a + pre_g)/2
                g = np.sqrt(a*pre_g)
            return a
        else:
            return (d(k-1, i) - 4**(-k) * d(k-1, i-1))/(1 - 4**(-k))
    return (x - 1)/d(n, n)

print(fast_approx_ln(1.41, 5))

