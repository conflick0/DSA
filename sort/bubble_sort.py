def sort(inp):
    num_inp = len(inp)

    for epoch in range(num_inp-1):
        for i in range(num_inp-epoch-1):
            if inp[i] > inp[i+1]:
                tmp = inp[i]
                inp[i] = inp[i+1]
                inp[i + 1] = tmp

    return inp


def test(out, gt):
    for o, g in zip(out, gt):
        if o != g:
            print('test failure !')
    print('test pass !')


if __name__ == '__main__':
    inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    gt = [23, 23, 29, 34, 55, 66, 67, 78, 78, 79, 88, 89, 92, 96, 96, 100]

    print('inp:', inp)
    out = sort(inp)

    print('out:', out)
    test(out, gt)
