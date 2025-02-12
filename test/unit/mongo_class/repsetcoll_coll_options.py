# Classification (U)

"""Program:  repsetcoll_coll_options.py

    Description:  Unit testing of RepSetColl.coll_options in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_coll_options.py

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


class CollOpts():                               # pylint:disable=R0903

    """Class:  CollOpts

    Description:  Class stub holder for Coll class.

    Methods:
        options

    """

    def options(self):

        """Function:  options

        Description:  Stub for Coll.coll_options method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_query

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_pd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"

    def test_query(self):

        """Function:  test_query

        Description:  Test method.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollOpts()

        self.assertTrue(mongo.coll_options())


if __name__ == "__main__":
    unittest.main()
