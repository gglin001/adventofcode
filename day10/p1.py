import os
import numpy as np


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    # fp = f'{cur_dir}/sample.txt'
    with open(fp, 'r') as f:
        lines = f.readlines()

    s00 = '('
    s01 = ')'
    s10 = '['
    s11 = ']'
    s20 = '{'
    s21 = '}'
    s30 = '<'
    s31 = '>'
    ig = set(('\n'))

    x0 = set((s00, s10, s20, s30))
    x1 = set((s01, s11, s21, s31))

    def get_x(x):
        if x == s01:
            return s00
        elif x == s11:
            return s10
        elif x == s21:
            return s20
        elif x == s31:
            return s30

    def get_y(x):
        if x == s00:
            return s01
        elif x == s10:
            return s11
        elif x == s20:
            return s21
        elif x == s30:
            return s31

    def get_p(x):
        if x == s01:
            return 3
        elif x == s11:
            return 57
        elif x == s21:
            return 1197
        elif x == s31:
            return 25137

    points = []
    for _, line in enumerate(lines):
        ls = []
        for _, c in enumerate(line):
            if c in ig:
                continue
            elif c in x0:
                ls.append(c)
            else:
                x = get_x(c)
                xx = ls.pop()
                if x == xx:
                    pass
                else:
                    points.append(get_p(c))

    return np.sum(points)


if __name__ == '__main__':
    res = func()
    print(res)
