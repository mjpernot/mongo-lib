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
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_libs                               # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Disconnect():                                     # pylint:disable=R0903

    """Class:  Disconnect

    Description:  Class is a representation of disconnect class.

    Methods:
        __init__
        disconnect

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the Mail class.

        Arguments:

        """

    def disconnect(self):

        """Method:  disconnect

        Description:  Method is representation of disconnect method.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_list_entry
        test_single_entry

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
