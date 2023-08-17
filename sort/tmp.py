from utils import test

def _part(inp, lo, hi):
    pivot = inp[hi]
    next_idx = lo
    for i in range(lo, len(inp)-1):
        if inp[i] < pivot:
            inp[i], inp[next_idx] = inp[next_idx], inp[i]
            next_idx += 1
    inp[hi], inp[next_idx] = inp[next_idx], inp[hi]
    return next_idx

def _sort(inp, lo, hi):
    if lo <= hi:
        p_idx = _part(inp, lo, hi)
        _sort(inp, lo, p_idx-1)
        _sort(inp, p_idx+1, hi)
    return inp


def sort(inp):
    return _sort(inp, 0, len(inp)-1)



if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)