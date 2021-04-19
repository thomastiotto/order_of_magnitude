==================
Order of magnitude
==================
Pure Python 3 implementation to convert floats, lists of floats, NumPy arrays to International System
of Units (SI) strings.

Install by::

    pip install order-of-magnitude

Some examples::

    from order_of_magnitude import order_of_magnitude

    order_of_magnitude.oom(1.20679264e+19)
    # returns '12.1 E'
    order_of_magnitude.oom(1.20679264e+19, decimals=4)
    # returns '12.0679 E'
    order_of_magnitude.oom(np.logspace(3,6, num=10))
    # returns ['1.0 k', '2.2 k', '4.6 k', '10.0 k', '21.5 k', '46.4 k', '100.0 k', '215.4 k', '464.2 k', '1.0 M']
    order_of_magnitude.oom(np.logspace(3,6, num=10), prefix=True)
    # returns ['1.0  kilo', '2.2  kilo', '4.6  kilo', '10.0  kilo', '21.5  kilo', '46.4  kilo', '100.0  kilo', '215.4  kilo', '464.2  kilo', '1.0  mega']

