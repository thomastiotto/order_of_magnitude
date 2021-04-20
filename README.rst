==================
Order of magnitude
==================
Pure Python 3 implementation to convert floats, lists of floats, NumPy arrays to International System
of Units (SI) strings.

Install by::

    pip install order-of-magnitude


Available functions
-------------------
- ``order_of_magnitude(x)``: returns the order of magnitude exponent of the input values as ``float``
- ``power_of_ten(x)``: returns the power of ten corresponding to the order of magnitude of the input values as ``float``
- ``prefix(x, decimals=1, omit_x=None, word=False)``: returns the SI prefix corresponding to the order of magnitude
  of the input values as ``string``
- ``symbol(x, decimals=1, omit_x=None, word=False)``: returns the SI symbol corresponding to the order of magnitude
  of the input values as ``string``
- ``short_scale(x, decimals=1, omit_x=None, word=True)``: returns the short scale measure corresponding to the order
  of magnitude of the input values as ``string``
- ``long_scale(x, decimals=1, omit_x=None, word=True)``: returns the long scale measure corresponding to the order of
  magnitude of the input values as ``string``
- ``prefixes_dict()``: returns the dictionary mapping order of magnitude to prefixes
- ``symbols_dict()``: returns the dictionary mapping order of magnitude to symbols
- ``short_scale_dict()``: returns the dictionary mapping order of magnitude to short scale measures
- ``long_scale_dict()``: returns the dictionary mapping order of magnitude to long scale measures

``x`` can be a scalar, a list, or a NumPy array.
``decimals`` controls how many decimal points are printed.
``omit_x`` only returns the SI units without the corresponding input number.
``word`` controls if the printed output is in word-form or as a number.

Examples
--------
::

    from order_of_magnitude import order_of_magnitude

    print("Order of magnitude:", order_of_magnitude.order_of_magnitude([1.1e-24, 100e3, 0]))
    print("Power of ten:", order_of_magnitude.power_of_ten([1.1e-24, 100e3, 0]))
    print("Prefix:", order_of_magnitude.prefix([1.1e-24, 100e3, 0]))
    print("Symbol:", order_of_magnitude.symbol([1.1e-24, 100e3, 0]))
    print("Only symbol:", order_of_magnitude.symbol([1.1e-24, 100e3, 0], omit_x=True))
    print("Prefix in words:", order_of_magnitude.prefix([1.1e-24, 100e3, 0], word=True))
    print("Only prefix in words:", order_of_magnitude.prefix([1.1e-24, 100e3, 0], omit_x=True, word=True))
    print("Short scale:", order_of_magnitude.short_scale([1.1e-24, 100e3, 0]))
    print("Short scale in numbers:", order_of_magnitude.short_scale([1.1e-24, 100e3, 0], word=False))
    print("Long scale only OOM:", order_of_magnitude.long_scale([1.1e-24, 100e3, 0], omit_x=True))
    print("Long scale dictionary", order_of_magnitude.long_scale_dict())


    ## Output
    # Order of magnitude: [-24, 5, 0]
    # Power of ten: [1e-24, 100000.0, 1.0]
    # Prefix: ['1.1 quaco', '100.0 kilo', 'N/A']
    # Symbol: ['1.1 g', '100.0 k', 'N/A']
    # Only symbol: ['g', 'k', 'N/A']
    # Prefix in words: ['one point one quaco', 'one hundred kilo', 'N/A']
    # Only prefix in words: ['quaco', 'kilo', 'N/A']
    # Short scale: ['one point one septillionth', 'one hundred thousand', 'N/A']
    # Short scale in numbers: ['1.1 septillionth', '100.0 thousand', 'N/A']
    # Long scale only OOM: ['quadrillionth', 'thousand', 'N/A']
    # Long scale dictionary {24: 'quadrillion', 21: 'trilliard', 18: 'trillion', 15: 'billiard', 12: 'billion', 9: 'milliard', 6: 'million', 3: 'thousand', 2: 'hundred', 1: 'ten', -1: 'tenth', -2: 'hundredth', -3: 'thousandth', -6: 'millionth', -9: 'milliardth', -12: 'billionth', -15: 'billiardth', -18: 'trillionth', -21: 'trilliardth', -24: 'quadrillionth'}

