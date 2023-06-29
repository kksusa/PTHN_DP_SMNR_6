import check_module

variants = [((1, 8), (2, 3), (3, 2), (4, 7), (5, 5), (6, 2), (7, 4), (8, 6)),
            ((1, 4), (2, 7), (3, 5), (4, 3), (5, 1), (6, 6), (7, 8), (8, 2))]

for i in variants:
    print(check_module.check_queen_cut(i))
