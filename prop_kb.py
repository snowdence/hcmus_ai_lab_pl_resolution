
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
