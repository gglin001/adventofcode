import os
import numpy as np
import matplotlib.pyplot as plt


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    arr = np.loadtxt(fp, delimiter=',', dtype=np.int32)

    res = []
    for i in range(arr.min(), arr.max()):
        dis = np.abs(arr - i)
        weight = np.asarray([(1 + x) * x / 2 for x in dis])
        sum = np.sum(weight)
        res.append(sum)
    res = np.asarray(res)

    # plt.plot(np.arange(arr.min(), arr.max()), res)
    # plt.show()

    arnmin = np.argmin(res)
    print(f"arnmin: {arnmin}, res[arnmin]: {int(res[arnmin])}")
    return int(res[arnmin])


if __name__ == '__main__':
    res = func()
    print(res)
    # 99540554
