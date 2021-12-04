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
    df_mask_no = pd.Series([x for x in range(df_mask.shape[0] // 5) for i in range(5)])
    all_boards = set(x for x in range(df_mask.shape[0] // 5))
    boards = set()
    for number in numbers:
        df_mask[df == number] = 1
        for data, mask in zip(df.groupby(df_mask_no), df_mask.groupby(df_mask_no)):
            no = data[0]
            a_data = data[1]
            a_mask = mask[1]
            sum_col = a_mask.sum(0, numeric_only=True)
            sum_row = a_mask.sum(1, numeric_only=True)
            idx_col = sum_col[sum_col == 5]
            idx_row = sum_row[sum_row == 5]
            if not idx_col.empty:
                if no not in boards:
                    boards.add(no)
                    sum = a_data[a_mask == 0].sum().sum()
                    last = (int(sum), number)
            if not idx_row.empty:
                if no not in boards:
                    boards.add(no)
                    sum = a_data[a_mask == 0].sum().sum()
                    last = (int(sum), number)

        if boards == all_boards:
            return last[0] * last[1]


if __name__ == '__main__':
    res = func()
    print(res)
