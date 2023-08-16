from utils import test


def search(inp, target):
    inp = sorted(inp)
    lo = 0
    hi = len(inp) - 1

    while lo <= hi:
        mid = int((lo + hi)/2)
        if target == inp[mid]:
            return True
        elif target > inp[mid]:
            lo += 1
        else:
            hi -= 1
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
