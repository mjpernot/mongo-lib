#!/usr/bin/python
# Classification (U)

"""Program:  fetch_db_info.py

    Description:  Unit testing of fetch_db_info in mongo_class.py.

    Usage:
        test/unit/mongo_class/fetch_db_info.py

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
import mongo_class
import version

__version__ = version.__version__


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for Mongo class.

    Methods:
        __init__ -> Class initialization.
        adm_cmd -> Stub holder for mongo_class.adm_cmd attribute.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.mongo = None

    def adm_cmd(self, mongo):

        """Function:  adm_cmd

        Description:  Stub holder for mongo_class.adm_cmd method.

        Arguments:
            (input) mongo -> Mongo class.

        """

        self.mongo = mongo

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_db_info -> Test fetch_db_info method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongodb = Mongo()

    def test_fetch_db_info(self):

        """Function:  test_fetch_db_info

        Description:  Test fetch_db_info method.

        Arguments:

        """

        self.assertTrue(mongo_class.fetch_db_info(self.mongodb))


if __name__ == "__main__":
    unittest.main()
