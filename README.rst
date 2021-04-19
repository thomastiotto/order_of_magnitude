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
    order_of_magnitude.oom(np.logspace(5,12))
    # returns ['10.0 M', '13.9 M', '19.3 M', '26.8 M', '37.3 M', '51.8 M', '72.0 M', '1.0 M', '1.4 M', '1.9 M', '2.7 M', '3.7 M', '5.2 M', '7.2 M', '10.0 M', '13.9 M', '19.3 M', '26.8 M', '37.3 M', '51.8 M', '72.0 M', '10.0 G', '13.9 G', '19.3 G', '26.8 G', '37.3 G', '51.8 G', '72.0 G', '1.0 G', '1.4 G', '1.9 G', '2.7 G', '3.7 G', '5.2 G', '7.2 G', '10.0 G', '13.9 G', '19.3 G', '26.8 G', '37.3 G', '51.8 G', '72.0 G', '10.0 T', '13.9 T', '19.3 T', '26.8 T', '37.3 T', '51.8 T', '72.0 T', '1.0 T']
    order_of_magnitude.oom(np.logspace(5,12), prefix=True)
    # returns ['10.0  mega', '13.9  mega', '19.3  mega', '26.8  mega', '37.3  mega', '51.8  mega', '72.0  mega', '1.0  mega', '1.4  mega', '1.9  mega', '2.7  mega', '3.7  mega', '5.2  mega', '7.2  mega', '10.0  mega', '13.9  mega', '19.3  mega', '26.8  mega', '37.3  mega', '51.8  mega', '72.0  mega', '10.0  giga', '13.9  giga', '19.3  giga', '26.8  giga', '37.3  giga', '51.8  giga', '72.0  giga', '1.0  giga', '1.4  giga', '1.9  giga', '2.7  giga', '3.7  giga', '5.2  giga', '7.2  giga', '10.0  giga', '13.9  giga', '19.3  giga', '26.8  giga', '37.3  giga', '51.8  giga', '72.0  giga', '10.0  tera', '13.9  tera', '19.3  tera', '26.8  tera', '37.3  tera', '51.8  tera', '72.0  tera', '1.0  tera']

