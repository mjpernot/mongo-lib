#!/usr/bin/python
# Classification (U)

"""Program:  Coll_coll_cnt.py

    Description:  Unit testing of Coll.coll_cnt in mongo_class.py.

    Usage:
        test/unit/mongo_class/Coll_coll_cnt.py

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
        coll_cnt -> Stub for Coll.coll_cnt method.

    """

    def coll_cnt(self, qry):

        """Function:  coll_cnt

        Description:  Stub for DB.db.coll_cnt method.

        Arguments:
            (input) qry -> Query command.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_no_query -> Test with no query command.

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
        self.coll = "coll_name"
        self.db_auth = None


    def test_no_query(self):

        """Function:  test_no_query

        Description:  Test with no query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port)
        mongo.db = CollCnt()

        self.assertTrue(mongo.coll_cnt())


if __name__ == "__main__":
    unittest.main()
