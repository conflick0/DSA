import math

from utils import test


def search(inp, target):
    inp = sorted(inp)
    lo = 0
    hi = len(inp) - 1

    while lo <= hi:
        # 與 binary 只差異於用斜率計算 mid
        mid = math.floor((target - inp[lo]) * (hi - lo) // (inp[hi] - inp[lo]) + lo)
        if mid > len(inp)-1:
            return False
        if inp[mid] == target:
            return True
        if target > inp[mid]:
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
