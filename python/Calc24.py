from itertools import permutations

formulas = (
    # a op b op c op d
    "{0} {1} {2} {3} {4} {5} {6}",

    # (a op b) op c op d
    "({0} {1} {2}) {3} {4} {5} {6}",
    # (a op b op c) op d
    "({0} {1} {2} {3} {4}) {5} {6}",
    # ((a op b) op c) op d
    "(({0} {1} {2}) {3} {4}) {5} {6}",
    # (a op (b op c)) op d
    "({0} {1} ({2} {3} {4}) {5} {6}",
    # (a op b) op (c op d)
    "({0} {1} {2}) {3} ({4} {5} {6})",

    # a op (b op c) op d
    "{0} {1} ({2} {3} {4}) {5} {6}",
    # a op (b op c op d)
    "{0} {1} ({2} {3} {4} {5} {6})",
    # a op ((b op c) op d)
    "{0} {1} (({2} {3} {4}) {5} {6})",

    # a op b op (c op d)
    "{0} {1} {2} {3} ({4} {5} {6})"
)

operators = ('+', '-', '*', '/')


def cal_24(l):
    cnt = 0
    for formula in formulas:
        for vals in permutations(l):
            for ops in permutations(operators, 3):
                show_str = formula.format(vals[0], ops[0], vals[1], ops[1], vals[2], ops[2], vals[3])
                str = formula.format(float(vals[0]), ops[0], float(vals[1]), ops[1], float(vals[2]), ops[2], float(vals[3]))
                try:
                    ret = eval(str)
                except :
                    continue
                if float(ret) == float(24):
                    cnt += 1
                    print("{0}: {1} = 24".format(cnt, show_str))

cal_24([2,4,6,8])




