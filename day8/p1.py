from functools import partial
import os
import numpy as np
import pandas as pd


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    # fp = f'{cur_dir}/sample.txt'
    df: pd.DataFrame = pd.read_csv(
        fp,
        header=None,
        sep=r'[ |]',
        dtype=str,
        engine='python',
    )
    df = df.iloc[:, -4:]

    def helper(patterns, x):
        if len(x) in patterns:
            return 1
        else:
            return 0

    patterns = set([2, 3, 4, 7])
    mask = df.applymap(partial(helper, patterns))
    return mask.sum().sum()


if __name__ == '__main__':
    res = func()
    print(res)
