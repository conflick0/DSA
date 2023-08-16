from utils import test


def search(inp, target):
    for i in inp:
        if i == target:
            return True
    return False


if __name__ == '__main__':
    inp = [75, 50, 60, 20, 90, 40, 80]
    targets = [20, 99]
    exps = [True, False]

    print('inp:', inp)
    outs = []
    for t in targets:
        out = search(inp, t)
        outs.append(out)
        print('target:', t)
        print('out:', out)

    test(outs, exps)
