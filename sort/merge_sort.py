from utils import test


def merge(left_ls, right_ls):
    result = []

    # 把比較小的 pop 出來，放入 result 陣列，直到左右陣列有一邊為空
    while len(left_ls) and len(right_ls):
        if left_ls[0] < right_ls[0]:
            result.append(left_ls.pop(0))
        else:
            result.append(right_ls.pop(0))

    # while 迴圈結束，表示左右陣列其中一個為空，因此左右判斷 concat 哪邊
    return result + left_ls if len(left_ls) else result + right_ls


def sort(inp):
    if len(inp) < 2:
        return inp

    size = len(inp)
    mid = size // 2

    left_ls = inp[:mid]
    right_ls = inp[mid:]

    # 遞迴呼叫
    return merge(sort(left_ls), sort(right_ls))


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)