from utils import test

def sort(inp):
    '''
    將下一個值(i+1)佔存起來(key)
    i = j
    如果目前值(j) > 下一個值(key), 將目前值往右位移一格，原本位置上空出位置 (j)
    目前 j, 往左位移一格變成 j-1
    再次檢查，當 key >= 目前值(j-1)，將 key 插入空位即為 inp[j + 1] = key
    ex.
    <>: i
    []: i+1
    step 0: 30, 40, <60>, [50]. key=50, j=i
    step 1: 30, <40>, [  ], 60. key=50, inp[j + 1] = inp[j], j-=1,
    step 2: 30, <40>, [50], 60. key=50, inp[j + 1] = key
    '''
    size = len(inp)
    for i in range(size - 1):
        key = inp[i + 1]
        j = i
        # 下一個值<目前值目就右移，直到下一個值沒有大於目前值
        while j >= 0 and key < inp[j]:
            # 右移
            inp[j + 1] = inp[j]
            # idx 往左
            j -= 1
        # 插入值，到空位
        inp[j + 1] = key
    return inp


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)
