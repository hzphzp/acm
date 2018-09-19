def max_mul(n: int):
    ''' this is a function that compute the max mutiplut result of the numbers divided by this integer
    '''
    result = []
    for i in range(n):
        if len(result) == 0:
            toadd = 1
            result.append(toadd)
            continue
        toadd = max([result[x] * result[-x-1] for x in range(int(len(result)/2) + 1)])
        result.append(max(toadd, i + 1))
    return result.pop(-1)


if __name__ == '__main__':
    print(max_mul(25))
    print(help(max_mul))