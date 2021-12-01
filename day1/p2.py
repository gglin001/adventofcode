import os
import numpy as np


def func(data):
    data0 = np.pad(data, [(0, 3)], constant_values=0)
    data1 = np.pad(data, [(1, 2)], constant_values=0)
    data2 = np.pad(data, [(2, 1)], constant_values=0)
    sum0 = data0 + data1 + data2
    diff = np.diff(sum0[2:-2])
    increased = np.size(diff[diff > 0])
    return increased


def load_input():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    arr = np.loadtxt(fp).astype(np.int32)
    return arr


if __name__ == '__main__':
    data = load_input()
    res = func(data)
    print(res)
