def move_zeros(lst):
    return [n for n in lst if n != 0 or isinstance(n, bool)] + [0] * lst.count(0)
