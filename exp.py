class ExprItem:
    encode_val = -1
    label_variable = "*"
    op = "+"

    def __init__(self, variable):
        variable = str(variable)
        if variable != None:
            if variable[0] in ["-", "+"]:
                # negative
                self.op = variable[0]
                self.label_variable = variable[1:]
            else:
                self.op = "+"
                self.label_variable = variable[:]

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.op == other.op and self.label_variable == other.label_variable

    def __invert__(self):
        op = "+" if self.op == "-" else "-"
        return ExprItem(op+self.label_variable)

    def __lt__(self, other):
        return (self.label_variable < other.label_variable)

    def __str__(self):
        return (self.op if self.op != '+' else '') + self.label_variable

    def __repr__(self):
        return self.op + self.label_variable


if __name__ == "__main__":
    print("Expr ==== main() ====")
    list_sort = ['A', 'B', 'C', '-D', 'E', '-A']
    list_sort_obj = [ExprItem(item) for item in list_sort]
    list_sort_obj.sort()
    print(list_sort_obj)
    print("End expr")
