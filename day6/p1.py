import os
import numpy as np
from collections import Counter


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    arr = np.loadtxt(fp, delimiter=',', dtype=np.int32)
    dic = dict(Counter(arr))
    for i in range(9):
        if i not in dic:
            dic[i] = 0

    for i in range(80):
        dic0 = dic[0]
        dic[0] = dic[1]
        dic[1] = dic[2]
        dic[2] = dic[3]
        dic[3] = dic[4]
        dic[4] = dic[5]
        dic[5] = dic[6]
        dic[6] = dic[7]
        dic[7] = dic[8]
        dic[8] = dic0
        dic[6] += dic0

    sum = 0
    for x in dic.values():
        sum += x
    return sum


if __name__ == '__main__':
    res = func()
    print(res)
