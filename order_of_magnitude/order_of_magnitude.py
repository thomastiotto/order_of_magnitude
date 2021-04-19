def oom(x, prefix=False, decimals=1):
    import operator
    import math

    def closest(search_key):
        closest_key = min(oom.keys(), key=lambda key: abs(key - search_key)) or oom[search_key]
        if closest_key in oom:
            return closest_key
        if closest_key >= len(oom):
            return len(oom)
        return list(oom.keys())[list(oom).index(closest_key) + 1] \
            if list(oom).index(closest_key) + 1 < len(oom) else closest_key

    def fexp(f):
        return int(math.floor(math.log10(abs(f)))) if f != 0 else 0

    def fman(f):
        return f / 10**fexp(f)

    if prefix:
        oom = {
                18 : " exa",
                15 : " peta",
                12 : " tera",
                9  : " giga",
                6  : " mega",
                3  : " kilo",
                2  : " hecto",
                1  : " deca",
                -1 : " deci",
                -2 : " centi",
                -3 : " mili",
                -6 : " micro",
                -9 : " nano",
                -12: " pico",
                -15: " femto",
                -18: " atto",
                -21: " zepto",
                -23: " quaco",
                }
    else:
        oom = {
                18 : "E",
                15 : "P",
                12 : "T",
                9  : "G",
                6  : "M",
                3  : "k",
                2  : "h",
                1  : "da",
                -1 : "d",
                -2 : "c",
                -3 : "m",
                -6 : "µ",
                -9 : "n",
                -12: "p",
                -15: "f",
                -18: "a",
                -21: "z",
                -23: "g",
                }

    if not isinstance(x, list):
        x = [x]

    ooms = list(map(lambda x: int(math.floor(math.log10(x))), x))
    ooms_matched = list(map(closest, ooms))
    diff = list(map(abs, map(operator.sub, ooms, ooms_matched)))
    res_string = [f"{fman(i) * int(math.pow(10, exp)):.{decimals}f} {oom[o]}" for i, exp, o in
                  zip(x, diff, ooms_matched)]

    return res_string if len(res_string) > 1 else res_string[0]
