

def issubset(this, other):
    for e in this:
        if e not in other:
            return False
    return True


def removeall(item, seq):
    if isinstance(seq, str):
        return seq.replace(item, '')
    else:
        return [x for x in seq if x != item]


def union(this, other):
    return type(this)(list(this) + list(other))


def unique(seq):
    return list(set(seq))


def check_complementary(dnew):
    pairs = [(dnew[i], dnew[j]) for i in range(len(dnew))
             for j in range(i+1, len(dnew))]
    for (ci, cj) in pairs:
        if ci == ~cj:
            return False
    return True
