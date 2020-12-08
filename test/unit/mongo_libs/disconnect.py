#!/usr/bin/python
# Classification (U)

"""Program:  disconnect.py

    Description:  Unit testing of disconnect in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/disconnect.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mongo_libs
import version

__version__ = version.__version__


class Disconnect(object):

    """Class:  Disconnect

    Description:  Class is a representation of disconnect class.

    Methods:
        __init__ -> Initialize configuration environment.
        disconnect -> Method is representation of disconnect method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Mail class.

        Arguments:

        """

        pass

    def disconnect(self):

        """Method:  disconnect

        Description:  Method is representation of disconnect method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Unit testing initilization.
        test_list_entry -> Test with disconnect in list.
        test_single_entry -> Test with single disconnect.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.inst = Disconnect()

    def test_list_entry(self):

        """Function:  test_list_entry

        Description:  Test with disconnect in list.

        Arguments:

        """

        self.assertFalse(mongo_libs.disconnect([self.inst]))

    def test_single_entry(self):

        """Function:  test_single_entry

        Description:  Test with single disconnect.

        Arguments:

        """

        self.assertFalse(mongo_libs.disconnect(self.inst))


if __name__ == "__main__":
    unittest.main()
