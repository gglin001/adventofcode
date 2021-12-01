import os
import numpy as np


def func(data):
    diff = np.diff(data)
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
