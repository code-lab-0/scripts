#!/usr/bin/env python3


import doctest
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
            if o == "--test" or "-t":
                doctest.testmod()
                break
            if o == "--help" or "-h":
                usage()
                break
        
        say_hello()

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





if __name__=="__main__":
    main(sys.argv[1:])

