import sys

def itoBase1(nb, base):
    nb = int(nb)
    if nb < 0:
        raise Exception('First argument less than zero')
    res = []
    while nb >= len(base):
        nb, n = divmod(nb, len(base))
        res.append(n)
    res.append(nb)
    return ''.join([base[i] for i in res[::-1]])


def itoBase2(nb, baseSrc, baseDst):
    return itoBase1(sum([int(baseSrc.index(i)*len(baseSrc)**n) 
                    for n, i in enumerate(reversed(nb))]), baseDst)


def itoBase(*args):
    if len(args) == 2:
        return itoBase1(*args)
    elif len(args) == 3:
        return itoBase2(*args)
    else:
        raise Exception('No such arguments count')


def main():
    print(itoBase(*sys.argv[1:]))


if __name__ == '__main__':
    try:
        main()
    except:
        print('usage')
