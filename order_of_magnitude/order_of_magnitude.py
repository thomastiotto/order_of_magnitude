import math
import operator
from numbers import Number


def __fexp( f ):
    return int( math.floor( math.log10( abs( f ) ) ) ) if f != 0 else 0


def __fman( f ):
    return f / 10**__fexp( f )


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
        0  : "",
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
__prefixes_inverted = {
        "yotta": 24,
        "zetta": 21,
        "exa"  : 18,
        "peta" : 15,
        "tera" : 12,
        "giga" : 9,
        "mega" : 6,
        "kilo" : 3,
        "hecto": 2,
        "deca" : 1,
        "deci" : -1,
        "centi": -2,
        "mili" : -3,
        "micro": -6,
        "nano" : -9,
        "pico" : -12,
        "femto": -15,
        "atto" : -18,
        "zepto": -21,
        "quaco": -24,
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
        0  : "",
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
__symbols_inverted = {
        "Y" : 24,
        "Z" : 21,
        "E" : 18,
        "P" : 15,
        "T" : 12,
        "G" : 9,
        "M" : 6,
        "k" : 3,
        "h" : 2,
        "da": 1,
        "d" : -1,
        "c" : -2,
        "m" : -3,
        "µ" : -6,
        "n" : -9,
        "p" : -12,
        "f" : -15,
        "a" : -18,
        "z" : -21,
        "g" : -24,
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
        0  : "",
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
__short_scale_inverted = {
        "septillion"   : 24,
        "sextillion"   : 21,
        "quintillion"  : 18,
        "quadrillion"  : 15,
        "trillion"     : 12,
        "billion"      : 9,
        "million"      : 6,
        "thousand"     : 3,
        "hundred"      : 2,
        "ten"          : 1,
        "tenth"        : -1,
        "hundredth"    : -2,
        "thousandth"   : -3,
        "millionth"    : -6,
        "billionth"    : -9,
        "trillionth"   : -12,
        "quadrillionth": -15,
        "quintillionth": -18,
        "sextillionth" : -21,
        "septillionth" : -24
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
        0  : "",
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
__long_scale_inverted = {
        "quadrillion"  : 24,
        "trilliard"    : 21,
        "trillion"     : 18,
        "billiard"     : 15,
        "billion"      : 12,
        "milliard"     : 9,
        "million"      : 6,
        "thousand"     : 3,
        "hundred"      : 2,
        "ten"          : 1,
        "tenth"        : -1,
        "hundredth"    : -2,
        "thousandth"   : -3,
        "millionth"    : -6,
        "milliardth"   : -9,
        "billionth"    : -12,
        "billiardth"   : -15,
        "trillionth"   : -18,
        "trilliardth"  : -21,
        "quadrillionth": -24,
        }


def __compute_oom( x, dictionary ):
    def closest( search_key ):
        if search_key in dictionary:
            return search_key
        for k in dictionary.keys():
            if search_key > k:
                return k
        if search_key > max( dictionary ):
            return max( dictionary )
        if search_key < min( dictionary ):
            return min( dictionary )
    
    ooms = list( map( lambda x: int( math.floor( math.log10( x ) if x != 0 else 0 ) ), x ) )
    ooms_matched = list( map( closest, ooms ) )
    diff = list( map( operator.sub, ooms, ooms_matched ) )
    
    return ooms, ooms_matched, diff


def __compute_oom_reference( x, ref_scale ):
    from collections import ChainMap
    
    if isinstance( ref_scale, Number ):
        scaler = __fexp( ref_scale )
    
    if isinstance( ref_scale, str ):
        m = ChainMap( __prefixes_inverted, __symbols_inverted, __short_scale_inverted, __long_scale_inverted )
        try:
            scaler = m[ ref_scale ]
        except KeyError:
            raise KeyError( f"{ref_scale} is not a valid SI measure" )
    
    ooms = list( map( lambda x: int( math.floor( math.log10( x ) if x != 0 else 0 ) ), x ) )
    ooms_matched = [ scaler for i in x ]
    diff = list( map( operator.sub, ooms, ooms_matched ) )
    
    return ooms, ooms_matched, diff


def __return_oom( x, dictionary, decimals, ref_scale, word ):
    from num2words import num2words
    
    if isinstance( x, Number ):
        x = [ x ]
    
    if ref_scale:
        ooms, ooms_matched, diff = __compute_oom_reference( x, ref_scale )
    else:
        ooms, ooms_matched, diff = __compute_oom( x, dictionary )
    
    if word:
        res_string = [ f"{num2words( __fman( i ) * math.pow( 10, exp ) )} {dictionary[ o ]}"
                       for i, exp, o in zip( x, diff, ooms_matched ) ]
    else:
        res_string = [ f"{__fman( i ) * math.pow( 10, exp ):.{decimals}f} {dictionary[ o ]}"
                       for i, exp, o in zip( x, diff, ooms_matched ) ]
    
    res_scale = [ math.pow( 10, o ) for o in ooms_matched ]
    res_oom = [ dictionary[ o ] for o in ooms_matched ]
    
    return (res_scale, res_oom, res_string) if len( res_string ) > 1 \
        else (res_scale[ 0 ], res_oom[ 0 ], res_string[ 0 ])


def order_of_magnitude( x ):
    if isinstance( x, Number ):
        x = [ x ]
    
    res = list( map( lambda x: int( math.floor( math.log10( x ) if x != 0 else 0 ) ), x ) )
    
    return res if len( res ) > 1 else res[ 0 ]


def power_of_ten( x ):
    if isinstance( x, Number ):
        x = [ x ]
    
    exps = list( map( __fexp, x ) )
    
    res = [ math.pow( 10, exp ) for exp in exps ]
    
    return res if len( res ) > 1 else res[ 0 ]


def convert( x, scale ):
    from collections import ChainMap
    
    if isinstance( x, Number ):
        x = [ x ]
    
    ooms = power_of_ten( x )
    
    if isinstance( scale, Number ):
        scaler = __fexp( scale )
    
    if isinstance( scale, str ):
        m = ChainMap( __prefixes_inverted, __symbols_inverted, __short_scale_inverted, __long_scale_inverted )
        try:
            scaler = m[ scale ]
        except KeyError:
            raise KeyError( f"{scale} is not a valid SI measure" )
    scaler *= -1
    res = [ el * math.pow( 10, scaler ) for el in x ]
    
    return res


def prefix( x, decimals=1, scale=None, word=False ):
    return __return_oom( x, __prefixes, decimals, scale, word=word )


def symbol( x, decimals=1, scale=None, word=False ):
    return __return_oom( x, __symbols, decimals, scale, word=word )


def short_scale( x, decimals=1, scale=None, word=True ):
    return __return_oom( x, __short_scale, decimals, scale, word=word )


def long_scale( x, decimals=1, scale=None, word=True ):
    return __return_oom( x, __long_scale, decimals, scale, word=word )


def prefixes_dict():
    return __prefixes


def symbols_dict():
    return __symbols


def short_scale_dict():
    return __short_scale


def long_scale_dict():
    return __long_scale
