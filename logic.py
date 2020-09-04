import numpy as np
import time
from itertools import groupby
from exp import *
from utils import *
from io_parser import IOParser
from input_parser import InputParser


class PropKB(object):
    clauses = []

    def __init__(self):
        self.clauses = []

    def tell_batch(self, batch):
        for item in batch:
            self.tell(item)

    def tell(self, sentence):
        self.clauses.append([ExprItem(item) for item in sentence])

    def solve(self, assumtion):
        print("Solve")


def pl_resolution(KB: PropKB, alpha):
    rslt_data_epoch = []
    clauses = KB.clauses
    alpha_query = [~ExprItem(item) for item in alpha]
    clauses.append(alpha_query)
    new = []
    epoch_arr = []
    while True:
        epoch_arr = []
        n = len(clauses)

        pairs = [(clauses[i], clauses[j])
                 for i in range(n) for j in range(i+1, n)]

        pairs_count = 0
        for (ci, cj) in pairs:
            pairs_count += 1
            resolvents = pl_resolve(ci, cj)

            new = union(new, resolvents)

            if '{}' in resolvents:
                counter = 0
                for c in new:
                    if c not in clauses:
                        clauses.append(c)
                        epoch_arr.append(c)
                        print(c)
                        counter += 1
                print("-------- ADDED {0} -----------".format(counter))
                rslt_data_epoch.append(epoch_arr)
                return (True, rslt_data_epoch)

        for item in new:
            item.sort()

        if issubset(new, clauses):
            print(
                "-------- ADDED {0} -----------".format(0))
            rslt_data_epoch.append([])
            return (False, rslt_data_epoch)

        # print('new:', len(new))
        counter = 0
        for c in new:
            if c not in clauses:
                clauses.append(c)
                epoch_arr.append(c)
                print(c)
                counter += 1
        print("-------- ADDED {0} -----------".format(counter))
        rslt_data_epoch.append(epoch_arr)


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
            if di == ~dj or ~di == dj:
                dnew = unique(removeall(di, ci) +
                              removeall(dj, cj))
                if len(dnew) == 0:
                    clauses.append('{}')
                else:
                    if check_complementary(dnew) == True:
                        clauses.append(dnew)
    # clauses.sort()
    return clauses


def output_result(path, rslt, list_clause):
    with open(path, 'w') as fs:
        for epoch in list_clause:
            fs.write("{}\n".format(len(epoch)))
            for clause in epoch:
                if clause == "{}":
                    fs.write("{}\n")
                else:
                    clause.sort()
                    if len(clause) > 1:
                        fs.write("{}\n".format(
                            ' OR '.join(str(e) for e in clause)
                        ))
                    else:
                        fs.write("{}\n".format(clause[0]))
        if rslt == True:
            fs.write("YES")
        else:
            fs.write("NO")


def run_test(case):
    kb = PropKB()
    p = IOParser()
    input_data: InputParser = p.load_input("input/{}.txt".format(case))
    kb.tell_batch(input_data.input_clauses)

    #kb.tell(['-A', 'B'])
    #kb.tell(['B', '-C'])
    #kb.tell(['A', '-B', 'C'])
    # kb.tell(['-B'])
    reslt, list_clause = pl_resolution(kb, input_data.query_alpha)
    output_result("output/{}.txt".format(case), reslt, list_clause)
    print('YES' if reslt else 'NO')


if __name__ == "__main__":
    print("Start")
    test_case = ["5"]
    for item in test_case:
        run_test(item)
    print("End")
