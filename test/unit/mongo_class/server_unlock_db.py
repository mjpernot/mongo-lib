#!/usr/bin/python
# Classification (U)

"""Program:  Server_unlock_db.py

    Description:  Unit testing of Server.unlock_db in mongo_class.py.

    Usage:
        test/unit/mongo_class/Server_unlock_db.py

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


class UnlockDb(object):

    """Class:  UnlockDb

    Description:  Class stub holder for Server class.

    Methods:
        unlock_db -> Stub holder for Server.conn.unlock_db method.

    """

    def unlock(self):

        """Function:  unlock

        Description:  Stub holder for Server.conn.unlock method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_unlock_db -> Test unlock_db method.

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
        self.dbs = "test"
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"

    def test_unlock_db(self):

        """Function:  test_unlock_db

        Description:  Test unlock_db method.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.passwd,
                                   self.host, self.port)
        mongo.conn = UnlockDb()

        self.assertTrue(mongo.unlock_db())


if __name__ == "__main__":
    unittest.main()
