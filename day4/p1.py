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
    df: pd.DataFrame
    df_mask: pd.DataFrame

    def helper(df: pd.DataFrame, df_mask: pd.DataFrame):
        for l, r in zip(left, right):
            a_mask = df_mask.iloc[l:r, :]
            sum0 = a_mask.sum(0, numeric_only=True)
            sum1 = a_mask.sum(1, numeric_only=True)
            idx0 = sum0[sum0 == 5]
            idx1 = sum1[sum1 == 5]
            if not idx0.empty:
                a_data = df.iloc[l:r, :]
                sum = a_data[a_mask == 0].sum().sum()
                return int(sum)
            if not idx1.empty:
                a_data = df.iloc[l:r, :]
                sum = a_data[a_mask == 0].sum().sum()
                return int(sum)
        return None

    for number in numbers:
        df_mask[df == number] = 1
        res = helper(df, df_mask)
        if res is not None:
            return number * res


if __name__ == '__main__':
    res = func()
    print(res)
