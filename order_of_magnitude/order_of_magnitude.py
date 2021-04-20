import math


def __fexp(f):
    return int(math.floor(math.log10(abs(f)))) if f != 0 else 0


def __fman(f):
    return f / 10**__fexp(f)


__prefixes = {
        24 : "yotta",
        21 : "zetta",
        18 : "exa",
        15 : "peta",
        12 : "tera",
        9  : "giga",
        6  : "mega",
        3  : "kilo",
        2  : "hecto",
        1  : "deca",
        -1 : "deci",
        -2 : "centi",
        -3 : "mili",
        -6 : "micro",
        -9 : "nano",
        -12: "pico",
        -15: "femto",
        -18: "atto",
        -21: "zepto",
        -24: "quaco",
        }
__symbols = {
        24 : "Y",
        21 : "Z",
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
        -24: "g",
        }
__short_scale = {
        24 : "septillion",
        21 : "sextillion",
        18 : "quintillion",
        15 : "quadrillion",
        12 : "trillion",
        9  : "billion",
        6  : "million",
        3  : "thousand",
        2  : "hundred",
        1  : "ten",
        -1 : "tenth",
        -2 : "hundredth",
        -3 : "thousandth",
        -6 : "millionth",
        -9 : "billionth",
        -12: "trillionth",
        -15: "quadrillionth",
        -18: "quintillionth",
        -21: "sextillionth",
        -24: "septillionth",
        }
__long_scale = {
        24 : "quadrillion",
        21 : "trilliard",
        18 : "trillion",
        15 : "billiard",
        12 : "billion",
        9  : "milliard",
        6  : "million",
        3  : "thousand",
        2  : "hundred",
        1  : "ten",
        -1 : "tenth",
        -2 : "hundredth",
        -3 : "thousandth",
        -6 : "millionth",
        -9 : "milliardth",
        -12: "billionth",
        -15: "billiardth",
        -18: "trillionth",
        -21: "trilliardth",
        -24: "quadrillionth",
        }


def __compute_oom(x, dictionary):
    import operator

    def closest(search_key):
        if search_key in dictionary:
            return search_key
        for k in dictionary.keys():
            if search_key > k:
                return k
        if search_key > max(dictionary):
            return max(dictionary)
        if search_key < min(dictionary):
            return min(dictionary)

    ooms = list(map(lambda x: int(math.floor(math.log10(x) if x != 0 else 0)), x))
    ooms_matched = list(map(closest, ooms))
    diff = list(map(abs, map(operator.sub, ooms, ooms_matched)))

    return ooms, ooms_matched, diff


def __return_oom(x, dictionary, decimals, omit_x, word):
    from num2words import num2words

    if isinstance(x, float):
        x = [x]

    ooms, ooms_matched, diff = __compute_oom(x, dictionary)

    if omit_x:
        res_string = [dictionary[o] if i != 0
                      else "N/A"
                      for i, exp, o in zip(x, diff, ooms_matched)]
    elif word:
        res_string = [f"{num2words(__fman(i) * int(math.pow(10, exp)))} {dictionary[o]}" if i != 0
                      else "N/A"
                      for i, exp, o in zip(x, diff, ooms_matched)]
    else:
        res_string = [f"{__fman(i) * int(math.pow(10, exp)):.{decimals}f} {dictionary[o]}" if i != 0
                      else "N/A"
                      for i, exp, o in zip(x, diff, ooms_matched)]

    return res_string if len(res_string) > 1 else res_string[0]


def order_of_magnitude(x):
    if isinstance(x, float):
        x = [x]

    res = list(map(lambda x: int(math.floor(math.log10(x) if x != 0 else 0)), x))

    return res if len(res) > 1 else res[0]


def power_of_ten(x):
    if isinstance(x, float):
        x = [x]

    exps = list(map(__fexp, x))

    res = [math.pow(10, exp) for exp in exps]
    return res if len(res) > 1 else res[0]


def prefix(x, decimals=1, omit_x=None, word=False):
    return __return_oom(x, __prefixes, decimals, omit_x, word=word)


def symbol(x, decimals=1, omit_x=None, word=False):
    return __return_oom(x, __symbols, decimals, omit_x, word=word)


def short_scale(x, decimals=1, omit_x=None, word=True):
    return __return_oom(x, __short_scale, decimals, omit_x, word=word)


def long_scale(x, decimals=1, omit_x=None, word=True):
    return __return_oom(x, __long_scale, decimals, omit_x, word=word)


def prefixes_dict():
    return __prefixes


def symbols_dict():
    return __symbols


def short_scale_dict():
    return __short_scale


def long_scale_dict():
    return __long_scale
