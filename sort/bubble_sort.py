from utils import test

def sort(inp):
    size = len(inp)
    # 執行 n - 1 個 epochs
    for epoch in range(size-1):
        # 執行 n - epoch - 1 個 epochs, 左邊大於右邊就交換
        for i in range(size-epoch-1):
            if inp[i] > inp[i+1]:
                tmp = inp[i]
                inp[i] = inp[i+1]
                inp[i + 1] = tmp

    return inp


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)
