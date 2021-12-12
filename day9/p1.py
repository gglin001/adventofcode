import os
import numpy as np


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    # fp = f'{cur_dir}/sample.txt'

    arr = np.loadtxt(fp, dtype=str)
    arr = np.asarray([[int(x) for x in y] for y in arr])
    h, w = arr.shape

    # create shift
    arr_p = np.pad(arr, ((1, 1), (1, 1)), constant_values=10)
    arr_t = np.pad(arr, ((2, 0), (1, 1)), constant_values=10)
    arr_b = np.pad(arr, ((0, 2), (1, 1)), constant_values=10)
    arr_l = np.pad(arr, ((1, 1), (2, 0)), constant_values=10)
    arr_r = np.pad(arr, ((1, 1), (0, 2)), constant_values=10)

    # get diff
    arr_ll = arr_p - arr_l
    arr_rr = arr_p - arr_r
    arr_bb = arr_p - arr_b
    arr_tt = arr_p - arr_t

    # get negative location
    set_ll = set(np.argwhere(arr_ll.flatten() < 0).flatten())
    set_rr = set(np.argwhere(arr_rr.flatten() < 0).flatten())
    set_bb = set(np.argwhere(arr_bb.flatten() < 0).flatten())
    set_tt = set(np.argwhere(arr_tt.flatten() < 0).flatten())
    locs = set_ll.intersection(set_rr).intersection(set_bb).intersection(set_tt)

    # get location in raw arr
    locs = np.asarray(list(locs), dtype=np.int32)
    locs_y = np.ceil(locs / (w + 2)) - 2
    locs_x = locs % (w + 2) - 1
    locs_y = locs_y.astype(np.int32)
    locs_x = locs_x.astype(np.int32)

    sum = 0
    for y, x in zip(locs_y, locs_x):
        sum = sum + arr[y, x] + 1
    return sum


if __name__ == '__main__':
    res = func()
    print(res)
