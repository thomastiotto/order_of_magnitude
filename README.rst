.. image:: https://badge.fury.io/py/order-of-magnitude.svg
    :target: https://badge.fury.io/py/order-of-magnitude

==================
Order of magnitude
==================
Pure Python 3 implementation to convert floats, lists of floats, NumPy arrays to International System
of Units (SI) strings.

Install by::

    pip install order-of-magnitude


Available functions
-------------------
- ``convert(x, scale)``: returns the input values as ``float`` in the scale provided
- ``order_of_magnitude(x)``: returns the order of magnitude exponent of the input values as ``float``
- ``power_of_ten(x)``: returns the power of ten corresponding to the order of magnitude of the input values as ``float``
- ``prefix(x, decimals=1, scale=None, omit_x=None, word=False)``: returns the SI prefix corresponding to the order of magnitude
  of the input values as ``string``
- ``symbol(x, decimals=1, scale=None, omit_x=None, word=False)``: returns the SI symbol corresponding to the order of magnitude
  of the input values as ``string``
- ``short_scale(x, decimals=1, scale=None, omit_x=None, word=True)``: returns the short scale measure corresponding to the order
  of magnitude of the input values as ``string``
- ``long_scale(x, decimals=1, scale=None, omit_x=None, word=True)``: returns the long scale measure corresponding to the order of
  magnitude of the input values as ``string``
- ``prefixes_dict()``: returns the dictionary mapping order of magnitude to prefixes
- ``symbols_dict()``: returns the dictionary mapping order of magnitude to symbols
- ``short_scale_dict()``: returns the dictionary mapping order of magnitude to short scale measures
- ``long_scale_dict()``: returns the dictionary mapping order of magnitude to long scale measures

Function parameters
-------------------
- ``x`` can be a scalar, a list, or a NumPy array.
- ``decimals`` controls how many decimal points are printed.
- ``scale`` sets the conversion to use a fixed reference SI unit.  Can be a ``float`` or an entry among the
  dictionary values returned by ``prefixes_dict()``, ``symbols_dict()``, ``short_scale_dict()``, or ``long_scale_dict
  ()``
- ``omit_x`` only returns the SI units without the corresponding input number.
- ``word`` controls if the printed output is in word-form or as a number.

Examples
--------
::

    from order_of_magnitude import order_of_magnitude

    print("Order of magnitude:", order_of_magnitude.order_of_magnitude([1.1e-3, 100e3, 0]))
    print("Power of ten:", order_of_magnitude.power_of_ten([1.1e-3, 100e3, 0]))
    print("Convert to mili:", order_of_magnitude.convert([1.1e-3, 100e3, 0], scale="mili"))
    print("Prefix:", order_of_magnitude.prefix([1.1e-3, 100e3, 0]))
    print("Prefix in mili:", order_of_magnitude.prefix([1.1e-3, 100e3, 0], scale="mili"))
    print("Prefix in kilo:", order_of_magnitude.prefix([1.1e-3, 100e3, 0], scale="k", decimals=8))
    print("Prefix in kilo:", order_of_magnitude.prefix([1.1e-3, 100e3, 0], scale=1e3))
    print("Symbol:", order_of_magnitude.symbol([1.1e-3, 100e3, 0]))
    print("Only symbol:", order_of_magnitude.symbol([1.1e-3, 100e3, 0], omit_x=True))
    print("Prefix in words:", order_of_magnitude.prefix([1.1e-3, 100e3, 0], word=True))
    print("Only prefix in words:", order_of_magnitude.prefix([1.1e-3, 100e3, 0], omit_x=True, word=True))
    print("Short scale:", order_of_magnitude.short_scale([1.1e-3, 100e3, 0]))
    print("Short scale in numbers:", order_of_magnitude.short_scale([1.1e-3, 100e3, 0], word=False))
    print("Long scale only OOM:", order_of_magnitude.long_scale([1.1e-3, 100e3, 0], omit_x=True))
    print("Long scale dictionary:", order_of_magnitude.long_scale_dict())

    ## Output
    # Order of magnitude: [-3, 5, 0]
    # Power of ten: [0.001, 100000.0, 1.0]
    # Convert to mili: [1.1, 100000000.0, 0.0]
    # Prefix: ['1.1 mili', '100.0 kilo', 'N/A']
    # Prefix in mili: ['1.1 mili', '100000000.0 mili', 'N/A']
    # Prefix in kilo: ['0.00000110 kilo', '100.00000000 kilo', 'N/A']
    # Prefix in kilo: ['0.0 kilo', '100.0 kilo', 'N/A']
    # Symbol: ['1.1 m', '100.0 k', 'N/A']
    # Only symbol: ['m', 'k', 'N/A']
    # Prefix in words: ['one point one mili', 'one hundred kilo', 'N/A']
    # Only prefix in words: ['mili', 'kilo', 'N/A']
    # Short scale: ['one point one thousandth', 'one hundred thousand', 'N/A']
    # Short scale in numbers: ['1.1 thousandth', '100.0 thousand', 'N/A']
    # Long scale only OOM: ['thousandth', 'thousand', 'N/A']
    # Long scale dictionary: {24: 'quadrillion', 21: 'trilliard', 18: 'trillion', 15: 'billiard', 12: 'billion', 9: 'milliard', 6: 'million', 3: 'thousand', 2: 'hundred', 1: 'ten', -1: 'tenth', -2: 'hundredth', -3: 'thousandth', -6: 'millionth', -9: 'milliardth', -12: 'billionth', -15: 'billiardth', -18: 'trillionth', -21: 'trilliardth', -24: 'quadrillionth'}

