import os
import numpy as np
import matplotlib.pyplot as plt


"""
TODO: 这是一个数值优化的问题, 尝试使用其他的方法
"""


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    arr = np.loadtxt(fp, delimiter=',', dtype=np.int32)

    res = []
    for i in range(arr.min(), arr.max()):
        sum = np.sum(np.abs(arr - i))
        res.append(sum)
    res = np.asarray(res)

    # plt.plot(np.arange(arr.min(), arr.max()), res)
    # plt.show()

    arnmin = np.argmin(res)
    print(f"arnmin: {arnmin}, res[arnmin]: {res[arnmin]}")
    return res[arnmin]


if __name__ == '__main__':
    res = func()
    print(res)
