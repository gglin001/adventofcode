import os
import numpy as np
import pandas as pd
from functools import partial


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'

    df: pd.DataFrame = pd.read_csv(
        fp,
        sep=r'[,>-]',
        skip_blank_lines=True,
        header=None,
        skipinitialspace=True,
    )
    df = df.drop(2, axis=1)
    df1 = df[df[0] == df[3]]
    df2 = df[df[1] == df[4]]
    df = df1.append(df2)

    x_max = df[[0, 3]].max().max()
    y_max = df[[1, 4]].max().max()
    mask = pd.DataFrame(np.zeros([x_max + 1, y_max + 1], dtype=np.int32))

    def helper(mask, row):
        x_loc_min, x_loc_max = row.iloc[[0, 2]].min(), row.iloc[[0, 2]].max()
        y_loc_min, y_loc_max = row.iloc[[1, 3]].min(), row.iloc[[1, 3]].max()
        mask.iloc[y_loc_min : y_loc_max + 1, x_loc_min : x_loc_max + 1] += 1

    df.apply(partial(helper, mask), axis=1)
    return (mask > 1).sum().sum()


if __name__ == '__main__':
    res = func()
    print(res)
