import os
import numpy as np
import pandas as pd


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    numbers = np.loadtxt(fp, delimiter=',', max_rows=1, dtype=np.int32)
    df = pd.read_csv(
        fp,
        sep=' ',
        skip_blank_lines=True,
        skiprows=[0],
        header=None,
        skipinitialspace=True,
        dtype=np.int32,
    )

    df_mask = pd.DataFrame(np.zeros(df.shape, dtype=np.int32))
    left = [x * 5 for x in range(df_mask.shape[0] // 5)]
    right = left[1:]
    right.append(df_mask.shape[0])
    stop = False
    for number in numbers:
        df_mask[df == number] = 1
        for l, r in zip(left, right):
            a_mask = df_mask.iloc[l:r, :]
            sum_col = a_mask.sum(0, numeric_only=True)
            sum_row = a_mask.sum(1, numeric_only=True)
            idx_col = sum_col[sum_col == 5]
            idx_row = sum_row[sum_row == 5]
            if not idx_col.empty:
                a_data = df.iloc[l:r, :]
                sum = a_data[a_mask == 0].sum().sum()
                stop = True
                break
            if not idx_row.empty:
                a_data = df.iloc[l:r, :]
                sum = a_data[a_mask == 0].sum().sum()
                stop = True
                break
        if stop:
            return int(sum) * number


if __name__ == '__main__':
    res = func()
    print(res)
