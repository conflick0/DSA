def test(out, exp):
    for o, e in zip(out, exp):
        if o != e:
            print('test fail!')
            return

    print('test success.')