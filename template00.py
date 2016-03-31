#!/usr/bin/env python3

"""
This example module shows various types of documentation available for use
with pydoc.  To generate HTML documentation for this module issue the
command:

    pydoc -w foo

"""

__author__ = "Osamu Ogasawara <mail@example.com>"
__version__ = "0.0.1"
__date__    = "01 November 2011"


import doctest

class Foo(object):
    """
    Foo encapsulates a name and an age.
    """
    def __init__(self, name, age):
        """
        Construct a new 'Foo' object.

        :param name: The name of foo
        :param age: The ageof foo
        :return: returns nothing
        """
        self.name = name
        self.age



"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""


def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> [factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000L
    >>> factorial(30L)
    265252859812191058636308480000000L
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000L

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # 1e300 のような値を捕らえる
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


import getopt
import sys

def usage():
    message="""
    template00.py - A template program for a simple python script.
    
    USAGE:
        python3 template00.py -t # invoke doctest.
    """

    print(message)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "htn:", ["help","test","name="])

        for o,a in opts:
            if o == "--name" or "-n":
                name = a
                say_hello()
            if o == "--test" or "-t":
                doctest.testmod()
                break
            if o == "--help" or "-h":
                usage()
                break
        

    except getopt.GetoptError:
        usage()
        sys.exit(2)




def say_hello():
    """This function prints a greeting message, and returns True.

    >>> say_hello()
    こんにちは
    True
    """
    print("こんにちは")
    #print("Hello")
    return True





if __name__ == "__main__":
    import doctest
    doctest.testmod()
    f = Foo('John Doe', 42)
    bar("hello world")



if __name__=="__main__":
    main(sys.argv[1:])

