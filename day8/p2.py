from functools import partial
import os
from typing import List
import pandas as pd


def is_defined(dir: List, x: str) -> bool:
    if x in dir:
        return True
    else:
        return False


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

    def helper(row):
        for x in row[:10]:
            if len(x) == 2:
                d1 = set(x)
            elif len(x) == 3:
                d7 = set(x)
            elif len(x) == 4:
                d4 = set(x)
            elif len(x) == 7:
                d8 = set(x)

        for x in row[:10]:
            x = set(x)
            if len(x) == 5:
                # d2 d3 d5
                if len(x.intersection(d1)) == 2:
                    d3 = x
                elif len(x.intersection(d4)) == 3:
                    d5 = x
                else:
                    d2 = x
            elif len(x) == 6:
                # d0 d6 d9
                if len(x.intersection(d4)) == 4:
                    d9 = x
                elif len(x.intersection(d1)) == 2:
                    d0 = x
                else:
                    d6 = x

        defined = partial(is_defined, dir())
        num = []
        for x in row[12:]:
            x = set(x)
            if len(x) == 2:
                num.append(1)
            elif len(x) == 3:
                num.append(7)
            elif len(x) == 4:
                num.append(4)
            elif len(x) == 7:
                num.append(8)
            elif len(x) == 5:
                if defined('d2') and x == d2:
                    num.append(2)
                elif defined('d3') and x == d3:
                    num.append(3)
                elif defined('d5') and x == d5:
                    num.append(5)
                else:
                    if not defined('d2'):
                        num.append(2)
                    elif not defined('d3'):
                        num.append(3)
                    elif not defined('d5'):
                        num.append(5)
                    else:
                        raise Exception('error')

            elif len(x) == 6:
                if defined('d0') and x == d0:
                    num.append(0)
                elif defined('d6') and x == d6:
                    num.append(6)
                elif defined('d9') and x == d9:
                    num.append(9)
                else:
                    if not defined('d0'):
                        num.append(0)
                    elif not defined('d6'):
                        num.append(6)
                    elif not defined('d9'):
                        num.append(9)
                    else:
                        raise Exception('error')

        num_str = "".join([str(x) for x in num])
        return int(num_str)

    mask = df.apply(helper, axis=1)
    return mask.sum()


if __name__ == '__main__':
    res = func()
    print(res)
