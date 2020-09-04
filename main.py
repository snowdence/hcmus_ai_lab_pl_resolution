import numpy as np
import time
from itertools import groupby


class PropKB(object):
    clauses = []

    def __init__(self):
        self.clauses = []

    def tell(self, sentence):
        self.clauses.append(sentence)

    def solve(self, assumtion):
        print("Solve")

    def retract(self, sentence):
        for c in sentence:
            if c in self.clauses:
                self.clauses.remove(c)


def pl_resolution(KB: PropKB, alpha):
    clauses = KB.clauses
    clauses.append([-alpha])
    new = []
    while True:
        n = len(clauses)
        print("Num clauses", n)

        pairs = [(clauses[i], clauses[j])
                 for i in range(n) for j in range(i+1, n)]
        print("Num pairs ", len(pairs))

        pairs_count = 0
        for (ci, cj) in pairs:
            pairs_count += 1
            resolvents = pl_resolve(ci, cj)
            if 'FALSE' in resolvents:
                return True
            new = union(new, resolvents)
        if issubset(new, clauses):
            return False

        print('new:', len(new))

        for c in new:
            if c not in clauses:
                c.sort()
                clauses.append(c)
                print("New", c)


def issubset(this, other):
    for e in this:
        if e not in other:
            return False
    return True


def removeall(item, seq):
    """Return a copy of seq (or string) with all occurences of item removed.
    >>> removeall(3, [1, 2, 3, 3, 2, 1, 3])
    [1, 2, 2, 1]
    >>> removeall(4, [1, 2, 3])
    [1, 2, 3]
    """
    if isinstance(seq, str):
        return seq.replace(item, '')
    else:
        return [x for x in seq if x != item]


def union(this, other):
    return type(this)(list(this) + list(other))


def unique(seq):
    """Remove duplicate elements from seq. Assumes hashable elements.
    >>> unique([1, 2, 3, 2, 1])
    [1, 2, 3]
    """
    return list(set(seq))


def pl_resolve(ci, cj):
    """Return all clauses that can be obtained by resolving clauses ci and cj.
    >>> for res in pl_resolve(to_cnf(A|B|C), to_cnf(~B|~C|F)):
    ...    ppset(disjuncts(res))
    set([A, C, F, ~C])
    set([A, B, F, ~B])
    """
    clauses = []
    for di in ci:
        for dj in cj:
            if di == -dj or -di == dj:
                dnew = unique(removeall(di, ci) +
                              removeall(dj, cj))
                if len(dnew) == 0:
                    clauses.append('FALSE')
                clauses.append(dnew)
    return clauses


if __name__ == "__main__":
    print("Stasrt")

    kb = PropKB()
    kb.tell([-1, 2])
    kb.tell([2, -3])
    kb.tell([1, -2, 3])
    kb.tell([-2])

    reslt = pl_resolution(kb, -1)
    print(reslt)
    print("End")
