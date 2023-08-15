from utils import test

def sort(inp):
    size = len(inp)
    for i in range(size-1):
        key = inp[i+1]
        j = i
        while j>=0 and key < inp[j]:
            inp[j+1] = inp[j]
            j-=1
        inp[j+1] = key
    return inp


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)