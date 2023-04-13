# Classification (U)

"""Program:  repsetcoll_coll_cnt.py

    Description:  Unit testing of RepSetColl.coll_cnt in mongo_class.py.

    Usage:
        test/unit/mongo_class/repsetcoll_coll_cnt.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class
import version

__version__ = version.__version__


class CollCnt(object):

    """Class:  CollCnt

    Description:  Class stub holder for RepSetColl class.

    Methods:
        __init__
        count
        count_documents

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class intialization.

        Arguments:

        """

        self.qry = None

    def count(self, qry):

        """Function:  count

        Description:  Stub holder for RepSetColl.db_coll.count method.

        Arguments:
            (input) qry

        """

        self.qry = qry

        return 10

    def count_documents(self, qry):

        """Function:  count_documents

        Description:  Stub holder for RepSetColl.db_coll.count_documents method

        Arguments:
            (input) qry

        """

        self.qry = qry

        return 10


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_qry
        test_no_qry

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

    def test_qry(self):

        """Function:  test_qry

        Description:  Test with query passed.

        Arguments:

        """

        qry = {"QueryHere"}
        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollCnt()

        self.assertEqual(mongo.coll_cnt(qry), 10)

    def test_no_qry(self):

        """Function:  test_no_qry

        Description:  Test with no query passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset)
        mongo.db_coll = CollCnt()

        self.assertEqual(mongo.coll_cnt(), 10)


if __name__ == "__main__":
    unittest.main()
