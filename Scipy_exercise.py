# This is exercise for scipy lecture.

# Nurullah Gulec 4 August 2020

import numpy as np


def bisect(f,a,b, tol=10e-5):
    # The purpose of the function is to code bisect recursively.
    upper=b
    lower=a
    middle=(upper+lower)/2
    if upper-lower< tol :
        return middle
    elif f(middle)>0 : # In this case the root is between lower and middle
        print(f'Current Mid Point = {middle}')
        return bisect(f,lower,middle)
    else:  # In this case the root is between middle and upper
        print(f'Current Mid Point = {middle}')
        return bisect(f, middle, upper)



f = lambda x: np.sin(4 * (x - 1/4)) + x + x**20 - 1
x = np.linspace(0, 1, 100)

print(bisect(f,0,1))

