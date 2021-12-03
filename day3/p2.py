import os
import numpy as np


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    arr = np.loadtxt(fp, dtype=str)

    arr1 = []
    for row in arr:
        arr1.append([1 if x == '1' else 0 for x in row])
    arr1 = np.asarray(arr1)

    def ff(arr, indexs):
        indexs = list(indexs)
        ones = []
        zeros = []
        h, w = arr.shape
        for i in range(w):
            ones_i = []
            zeros_i = []
            for j in indexs:
                if arr[j, i]:
                    ones_i.append(j)
                else:
                    zeros_i.append(j)
            ones.append(ones_i)
            zeros.append(zeros_i)
        return ones, zeros

    h, w = arr1.shape
    oxygen = set(x for x in range(h))
    for i in range(w):
        ones, zeros = ff(arr1, oxygen)
        if len(oxygen) == 1:
            break
        if len(ones[i]) >= len(zeros[i]):
            oxygen = oxygen.intersection(set(ones[i]))
        else:
            oxygen = oxygen.intersection(set(zeros[i]))
    ox = [1 if x else 0 for x in arr1[oxygen.pop()]]
    ox = int(''.join(str(x) for x in ox), 2)

    co2 = set(x for x in range(h))
    for i in range(w):
        ones, zeros = ff(arr1, co2)
        if len(co2) == 1:
            break
        if len(zeros[i]) > len(ones[i]):
            co2 = co2.intersection(set(ones[i]))
        else:
            co2 = co2.intersection(set(zeros[i]))
    co2 = [1 if x else 0 for x in arr1[co2.pop()]]
    co2 = int(''.join(str(x) for x in co2), 2)
    return ox * co2


if __name__ == '__main__':
    res = func()
    print(res)
    # 482500
