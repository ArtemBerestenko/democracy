__author__ = 'aberes'

import string

import random


def randstring(n):
    """
    Generate random string
    :param n: length of the string
    :return: generated string
    """
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])
