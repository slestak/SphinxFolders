#coding=utf-8

"""
Actual code of the sphinxfolders Python module.

"""
import gettext
import os.path
from sphinxfolders import __data_path__
gettext.install('sphinxfolders', os.path.join(__data_path__, 'locale'))


def sample_function(first, second=4):
    """This is a sample function to demonstrate doctests
    of :mod:`sphinxfolders.code` and docs.
    It only return the sum of its two arguments.

    Args:
      * `first` (:class:`int`): first value to add
      * `second` (:class:`int`): second value to add, 4 by default

    Returns:
      * :class:`int`: the sum of `first` and `second`.

    >>> sample_function(6, second=3)
    9
    >>> sample_function(6)
    10
    """
    return first + second


if __name__ == '__main__':
    import doctest
    doctest.testmod()
