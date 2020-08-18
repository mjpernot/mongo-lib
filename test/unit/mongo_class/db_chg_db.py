#!/usr/bin/python
# Classification (U)

"""Program:  DB_chg_db.py

    Description:  Unit testing of DB.chg_db in mongo_class.py.

    Usage:
        test/unit/mongo_class/DB_chg_db.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
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

    def test_database_passed(self):

        """Function:  test_database_passed

        Description:  Test with database passed.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japwd,
                               self.host, self.port)
        mongo.conn = {"testdb": "testdb"}
        mongo.chg_db("testdb")

        self.assertEqual((mongo.db, mongo.db_name), ("testdb", "testdb"))

    def test_no_database(self):

        """Function:  test_no_database

        Description:  Test with no database passed.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japwd,
                               self.host, self.port)
        mongo.conn = {"test": "testdb"}
        mongo.chg_db()

        self.assertEqual((mongo.db, mongo.db_name), ("testdb", "test"))


if __name__ == "__main__":
    unittest.main()
