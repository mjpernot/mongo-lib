#!/usr/bin/python
# Classification (U)

"""Program:  RepSetColl_coll_cnt.py

    Description:  Unit testing of RepSetColl.coll_cnt in mongo_class.py.

    Usage:
        test/unit/mongo_class/RepSetColl_coll_cnt.py

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

    Description:  Class stub holder for RepSetColl class.

    Super-Class:

    Sub-Classes:

    Methods:
        count -> Stub holder for RepSetColl.db_coll.count method.

    """

    def count(self, qry):

        """Function:  count

        Description:  Stub holder for RepSetColl.db_coll.count method.

        Arguments:
            (input) qry -> Mongo query statement.

        """

        return 10


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_qry -> Test with query passed.
        test_no_qry -> Test with no query passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.passwd = "mongo_pwd"
        self.host = "host_server"
        self.port = 27017
        self.db = "test"
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"

    def test_qry(self):

        """Function:  test_qry

        Description:  Test with query passed.

        Arguments:

        """

        qry = {"QueryHere"}
        mongo = mongo_class.RepSetColl(self.name, self.user, self.passwd,
                                       self.host, self.port,
                                       repset=self.repset)
        mongo.db_coll = CollCnt()

        self.assertEqual(mongo.coll_cnt(qry), 10)

    def test_no_qry(self):

        """Function:  test_no_qry

        Description:  Test with no query passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(self.name, self.user, self.passwd,
                                       self.host, self.port,
                                       repset=self.repset)
        mongo.db_coll = CollCnt()

        self.assertEqual(mongo.coll_cnt(), 10)


if __name__ == "__main__":
    unittest.main()
