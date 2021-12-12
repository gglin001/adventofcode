import os
from collections import Counter


def func():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    fp = f'{cur_dir}/input.txt'
    # fp = f'{cur_dir}/sample.txt'
    # fp = f'{cur_dir}/sample2.txt'
    # fp = f'{cur_dir}/sample3.txt'
    with open(fp, 'r') as f:
        lines = f.readlines()

    small = set()
    big = set()
    graph = dict()
    for line in lines:
        x, y = line.strip().split('-')
        for c in [x, y]:
            if c.isupper():
                big.add(c)
            elif c not in ['start', 'end']:
                small.add(c)

        if x in graph:
            graph[x].append(y)
        else:
            graph[x] = [y]

        if y in graph:
            graph[y].append(x)
        else:
            graph[y] = [x]

    fin_paths = []
    paths = []
    paths.append(['start'])
    for idx, path in enumerate(paths):
        # print(idx)
        last = path[-1]
        nexts = graph[last]
        for next in nexts:
            if next == 'start':
                continue

            if next == 'end':
                fin_paths.append([*path, next])
                continue

            if next in small:
                count = Counter([*path, next])
                small_count = [count[x] for x in small]

                if max(small_count) > 2:
                    continue

                if small_count.count(2) > 1:
                    continue

            paths.append([*path, next])

    return len(fin_paths)


if __name__ == '__main__':
    res = func()
    print(res)
