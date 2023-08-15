from utils import test

def sort(inp):
    size = len(inp)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            tmp = inp[i]
            j = i
            while j >= gap and tmp < inp[j-gap]:
                inp[j] = inp[j-gap]
                j -= gap
            inp[j] = tmp

        gap = gap // 2
    return inp


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)
