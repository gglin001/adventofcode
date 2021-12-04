import os
import numpy as np


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    arr_raw = np.loadtxt(fp, dtype=str)

    arr = []
    for row in arr_raw:
        arr.append([True if x == '1' else False for x in row])
    arr = np.asarray(arr)

    h, w = arr.shape
    ones = []
    zeros = []
    for i in range(w):
        ones_i = []
        zeros_i = []
        for j in range(h):
            if arr[j, i]:
                ones_i.append(j)
            else:
                zeros_i.append(j)
        ones.append(ones_i)
        zeros.append(zeros_i)

    gamma_rate = []
    epsilon = []
    for i in range(w):
        if len(ones[i]) > len(zeros[i]):
            gamma_rate.append(1)
            epsilon.append(0)
        else:
            gamma_rate.append(0)
            epsilon.append(1)
    ga = int(''.join(str(x) for x in gamma_rate), 2)
    eps = int(''.join(str(x) for x in epsilon), 2)
    return ga * eps


if __name__ == '__main__':
    res = func()
    print(res)
