__author__ = 'aberes'
from tests import registration_tests

# this is runner
def run_tests():
    from proboscis import TestProgram
    # from tests import unit

    # Run Proboscis and exit.
    TestProgram().run_and_exit()


if __name__ == '__main__':
    run_tests()
