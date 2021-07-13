#!/usr/bin/python
# Classification (U)

"""Program:  coll_coll_cnt.py

    Description:  Unit testing of Coll.coll_cnt in mongo_class.py.

    Usage:
        test/unit/mongo_class/coll_coll_cnt.py

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


class CollCnt(object):

    """Class:  CollCnt

    Description:  Class stub holder for Coll class.

    Methods:
        __init__
        count

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.qry = None

    def count(self, qry):

        """Function:  count

        Description:  Stub for Coll.coll_cnt method.

        Arguments:
            (input) qry

        """

        self.qry = qry

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_query
        test_empty_query
        test_no_query

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
        self.coll = "coll_name"
        self.db_auth = None

    def test_query(self):

        """Function:  test_query

        Description:  Test with query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port)
        mongo.coll = CollCnt()

        self.assertTrue(mongo.coll_cnt({"Key": "Value"}))

    def test_empty_query(self):

        """Function:  test_empty_query

        Description:  Test with empty query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port)
        mongo.coll = CollCnt()

        self.assertTrue(mongo.coll_cnt({}))

    def test_no_query(self):

        """Function:  test_no_query

        Description:  Test with no query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port)
        mongo.coll = CollCnt()

        self.assertTrue(mongo.coll_cnt())


if __name__ == "__main__":
    unittest.main()
