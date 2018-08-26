def biggerIsGreater(w):
    f = False
    for i in reversed(range(len(w))):
        if i != 0 and w[i-1] < w[i]:
            break
    if i == 0:
        return "no answer"
    else:
        left = w[:i-1]
        ex = w[i-1]
        right = w[i:]
        return left+exchange(ex, right)


def exchange(ex, right):
    lst = [x for x in right]
    lst.append(ex)
    lst.sort()
    newex = lst[lst.index(ex)+lst.count(ex)]
    lst.remove(newex)
    lst.insert(0, newex)
    return "".join(lst)
