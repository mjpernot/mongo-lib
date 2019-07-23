#!/usr/bin/python
# Classification (U)

"""Program:  Server_lock_db.py

    Description:  Unit testing of Server.lock_db in mongo_class.py.

    Usage:
        test/unit/mongo_class/Server_lock_db.py

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


class LockDb(object):

    """Class:  LockDb

    Description:  Class stub holder for Server class.

    Super-Class:

    Sub-Classes:

    Methods:
        fsync -> Stub holder for Server.conn.fsync method.

    """

    def fsync(self, lock):

        """Function:  fsync

        Description:  Stub holder for Server.conn.fsync method.

        Arguments:
            (input) lock -> Lock database.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_lock_db -> Test lock_db method.

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

    def test_lock_db(self):

        """Function:  test_lock_db

        Description:  Test lock_db method.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.passwd,
                                   self.host, self.port)
        mongo.conn = LockDb()

        self.assertTrue(mongo.lock_db(lock=True))


if __name__ == "__main__":
    unittest.main()
