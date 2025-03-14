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
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class                              # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Mongo():                                  # pylint:disable=R0903

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
        test_fetch_db_info

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mongo = Mongo()

    def test_fetch_db_info(self):

        """Function:  test_fetch_db_info

        Description:  Test fetch_db_info method.

        Arguments:

        """

        self.assertTrue(mongo_class.fetch_db_info(self.mongo))


if __name__ == "__main__":
    unittest.main()
