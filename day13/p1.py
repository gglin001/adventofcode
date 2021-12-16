import os
import numpy as np


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

    new_locs = set()
    axis, val = folds[0]
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

    return len(new_locs)


if __name__ == '__main__':
    res = func()
    print(res)
