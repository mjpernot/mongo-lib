#!/usr/bin/python
# Classification (U)

"""Program:  Coll_coll_find1.py

    Description:  Unit testing of Coll.coll_find1 in mongo_class.py.

    Usage:
        test/unit/mongo_class/Coll_coll_find1.py

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
        find_one -> Stub for Coll.coll_find1 method.

    """

    def find_one(self, qry):

        """Function:  find_one

        Description:  Stub for Coll.coll_find1 method.

        Arguments:
            (input) qry -> Query command.

        """

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
        self.passwd = "mongo_pwd"
        self.host = "host_server"
        self.port = 27017
        self.db = "test"
        self.coll = "coll_name"
        self.db_auth = None

    def test_query(self):

        """Function:  test_query

        Description:  Test with query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port)
        mongo.coll = CollFind()

        self.assertTrue(mongo.coll_find1({"Key": "Value"}))

    def test_empty_query(self):

        """Function:  test_empty_query

        Description:  Test with empty query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port)
        mongo.coll = CollFind()

        self.assertTrue(mongo.coll_find1({}))

    def test_no_query(self):

        """Function:  test_no_query

        Description:  Test with no query command.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port)
        mongo.coll = CollFind()

        self.assertTrue(mongo.coll_find1())


if __name__ == "__main__":
    unittest.main()
