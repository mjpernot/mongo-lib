# Classification (U)

"""Program:  fetch_cmd_line.py

    Description:  Unit testing of fetch_cmd_line in mongo_class.py.

    Usage:
        test/unit/mongo_class/fetch_cmd_line.py

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

# Local
sys.path.append(os.getcwd())
import mongo_class
import version

__version__ = version.__version__


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for Mongo class.

    Methods:
        __init__
        adm_cmd

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.mongodb = None

    def adm_cmd(self, mongo):

        """Function:  adm_cmd

        Description:  Stub holder for mongo_class.adm_cmd method.

        Arguments:
            (input) mongo

        """

        self.mongodb = mongo

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_fetch_cmd_line

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()

    def test_fetch_cmd_line(self):

        """Function:  test_fetch_cmd_line

        Description:  Test fetch_cmd_line method.

        Arguments:

        """

        self.assertTrue(mongo_class.fetch_cmd_line(self.mongo))


if __name__ == "__main__":
    unittest.main()
