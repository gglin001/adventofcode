import os
import numpy as np


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    # fp = f'{cur_dir}/sample.txt'
    arr = np.loadtxt(fp, dtype=str)
    arr = np.asarray([[np.int32(x) for x in y] for y in arr])
    H, W = arr.shape

    def get_win(h, w):
        wins = []
        if h > 0:
            wins.append((h - 1, w))
            if w > 0:
                wins.append((h - 1, w - 1))
            if w < W - 1:
                wins.append((h - 1, w + 1))
        if w > 0:
            wins.append((h, w - 1))
            if h < H - 1:
                wins.append((h + 1, w - 1))
        if w < W - 1:
            wins.append((h, w + 1))
            if h < H - 1:
                wins.append((h + 1, w + 1))
        if h < H - 1:
            wins.append((h + 1, w))
        return wins

    step = 0
    while True:
        step += 1
        flashes = 0
        arr += 1
        change = 1
        while change > 0:
            change -= 1
            for h in range(H):
                for w in range(W):
                    if arr[h, w] > 9:
                        flashes += 1
                        change += 1
                        arr[h, w] = -10
                        for hw in get_win(h, w):
                            arr[hw] += 1
        arr[arr < 0] = 0
        if flashes == H * W:
            break

    return step


if __name__ == '__main__':
    res = func()
    print(res)
