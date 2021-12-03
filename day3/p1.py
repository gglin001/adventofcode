import os
import numpy as np


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    arr = np.loadtxt(fp, dtype=str)

    arr1 = []
    for row in arr:
        arr1.append([True if x == '1' else False for x in row])
    arr1 = np.asarray(arr1)

    gamma_rate = []
    epsilon = []
    count, bits = arr1.shape
    for i in range(bits):
        if np.sort(arr1[:, i])[count // 2]:
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
