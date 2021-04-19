from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='order_of_magnitude',
        version='v1.2',
        packages=['order_of_magnitude'],
        url='https://github.com/Tioz90/order_of_magnitude',
        license='MIT',
        author='Thomas Tiotto',
        author_email='tioz1990@gmail.com',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        description='Converts floats to SI units.'
        )
