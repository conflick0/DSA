from utils import test

def max_heapify(inp, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # 與左節點比較大小，如果左節點大，取代 largest
    if l < n and inp[l] > inp[largest]:
        largest = l

    # largest 與 右節點比較大小，如果右節點大，取代 largest
    if r < n and inp[r] > inp[largest]:
        largest = r

    # largest 不是自己，將其值替換，重複遞迴
    if largest != i:
        inp[i], inp[largest] = inp[largest], inp[i]
        max_heapify(inp, n, largest)


def sort(inp):
    n = len(inp)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(inp, n, i)

    for i in range(n - 1, 0, -1):
        inp[i], inp[0] = inp[0], inp[i]
        max_heapify(inp, i, 0)

    return inp


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)
