from utils import test

def sort(inp):
    size = len(inp)
    # 執行 n - 1 個 epochs
    for i in range(size-1):
        # 尋找 i ~ n 最小值
        min_idx = i
        for j in range(i, size):
            if inp[min_idx] > inp[j]:
                min_idx = j
        # 將 inp[i] 與 最小值 替換
        inp[i], inp[min_idx] = inp[min_idx], inp[i]

    return inp


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)
