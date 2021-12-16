import os
import numpy as np
import pandas as pd


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    # fp = f'{cur_dir}/sample.txt'
    with open(fp, 'r') as f:
        lines = f.readlines()

    locs = set()
    folds = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        elif line.startswith('fold along '):
            folds.append([line[11:12], int(line[13:])])
        else:
            loc = tuple([int(x) for x in line.split(',')])
            locs.add(loc)

    def helper(locs, fold):
        new_locs = set()
        axis, val = fold
        if axis == 'x':
            for loc in locs:
                x, y = loc
                xx = x
                if x < val:
                    xx = x
                else:
                    xx = val + val - x
                new_loc = tuple([xx, y])
                new_locs.add(new_loc)
        elif axis == 'y':
            for loc in locs:
                x, y = loc
                yy = y
                if y < val:
                    yy = y
                else:
                    yy = val + val - y
                new_loc = tuple([x, yy])
                new_locs.add(new_loc)
        else:
            raise ValueError('error')
        return new_locs

    for fold in folds:
        locs = helper(locs, fold)

    arr = np.asarray(list(locs))
    x, y = arr.max(0)
    mask = np.zeros([y + 1, x + 1], dtype=np.int32)
    for loc in locs:
        x, y = loc
        mask[y, x] = 1

    df = pd.DataFrame(mask)
    df_str = df.to_string(header=None, index=None)
    df_str = df_str.replace('0', ' ')
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{cur_dir}/p2.txt", 'w') as f:
        f.write(df_str)

    return df_str


if __name__ == '__main__':
    res = func()
    print(res)
