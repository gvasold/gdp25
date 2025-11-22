def read_names(filename):
    with open(filename) as fh:
        names = [n.rstrip() for n in fh.readlines()]
    return names