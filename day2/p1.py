import os
import pandas as pd


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'

    df = pd.read_csv(fp, sep=' ', header=None)
    forward = df[df[0] == 'forward'][1].sum()
    down = df[df[0] == 'down'][1].sum()
    up = df[df[0] == 'up'][1].sum()
    return forward * (down - up)


if __name__ == '__main__':
    res = func()
    print(res)
