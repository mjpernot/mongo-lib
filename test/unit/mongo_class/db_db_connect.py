#!/usr/bin/python
# Classification (U)

"""Program:  DB_db_connect.py

    Description:  Unit testing of DB.db_connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/DB_db_connect.py

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


class DBConn(object):

    """Class:  DBConn

    Description:  Class stub holder for DB class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.test = "testdb"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_none_database_passed -> Test with none database passed.
        test_database_passed -> Test with database passed.
        test_no_database -> Test with no database passed.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japwd = "mongo_pwd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.db_auth = None

    def test_none_database_passed(self):

        """Function:  test_none_database_passed

        Description:  Test with none database passed.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japwd,
                               self.host, self.port)
        mongo.conn = DBConn()
        mongo.db_connect(dbs=None)

        self.assertEqual((mongo.db), ("testdb"))

    def test_database_passed(self):

        """Function:  test_database_passed

        Description:  Test with database passed.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japwd,
                               self.host, self.port)
        mongo.conn = {"testdb": "testdb"}
        mongo.db_connect("testdb")

        self.assertEqual((mongo.db), ("testdb"))

    def test_no_database(self):

        """Function:  test_no_database

        Description:  Test with no database passed.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japwd,
                               self.host, self.port)
        mongo.conn = {"test": "testdb"}
        mongo.db_connect()

        self.assertEqual((mongo.db), ("testdb"))


if __name__ == "__main__":
    unittest.main()
