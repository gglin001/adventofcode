import os
import pandas as pd


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    df = pd.read_csv(fp, sep=' ', header=None)

    depth = 0
    aim = 0
    horizontal = 0
    for _, row in df.iterrows():
        if row[0] == 'down':
            aim += row[1]
        elif row[0] == 'up':
            aim -= row[1]
        elif row[0] == 'forward':
            horizontal += row[1]
            depth += aim * row[1]
        else:
            raise ValueError('Error command')
    return depth * horizontal


if __name__ == '__main__':
    res = func()
    print(res)
