import numpy as np
import matplotlib.pyplot as plt
import inspect
from typing import Union

def retrieve_name(var, scope = 1):
    if scope is 1:
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    elif scope is 2:
        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]

def auto_subplot(*srcs, col = None):
    if isinstance(srcs, tuple) or isinstance(srcs, list):
        srcs = srcs[0]
    n = len(srcs)
    if col is None:
        col = int(np.ceil(np.sqrt(n)))
    row = int(np.ceil(n / col))
    names = []
    for i in range(len(srcs)):
        names.append(retrieve_name(srcs[i], scope = 2)[0])
    for i in range(n):
        plt.subplot(row, col, i+1)
        plt.imshow(srcs[i])
        plt.title(names[i])
    plt.show()
