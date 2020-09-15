#!/usr/bin/python
# Classification (U)

"""Program:  repsetcoll_coll_find1.py

    Description:  Unit testing of RepSetColl.coll_find1 in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_coll_find1.py

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


class CollFind(object):

    """Class:  CollFind

    Description:  Class stub holder for Coll class.

    Methods:
        __init__ -> Class initialization.
        find_one -> Stub for Coll.coll_find1 method.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.qry = None

    def find_one(self, qry):

        """Function:  find_one

        Description:  Stub for Coll.coll_find1 method.

        Arguments:
            (input) qry -> Query command.

        """

        self.qry = qry

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_query -> Test with query command.
        test_empty_query -> Test with empty query command.
        test_no_query -> Test with no query command.

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

        Description:  Test with query command.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollFind()

        self.assertTrue(mongo.coll_find1({"Key": "Value"}))

    def test_empty_query(self):

        """Function:  test_empty_query

        Description:  Test with empty query command.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollFind()

        self.assertTrue(mongo.coll_find1({}))

    def test_no_query(self):

        """Function:  test_no_query

        Description:  Test with no query command.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollFind()

        self.assertTrue(mongo.coll_find1())


if __name__ == "__main__":
    unittest.main()
