import os


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
            if next in small and next in path:
                continue

            if next == 'start':
                continue

            if next == 'end':
                fin_paths.append([*path, next])
                continue

            paths.append([*path, next])

    return len(fin_paths)


if __name__ == '__main__':
    res = func()
    print(res)
