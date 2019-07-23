#!/usr/bin/python
# Classification (U)

"""Program:  Server_fetch_dbs.py

    Description:  Unit testing of Server.fetch_dbs in mongo_class.py.

    Usage:
        test/unit/mongo_class/Server_fetch_dbs.py

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


class FetchAdr(object):

    """Class:  FetchAdr

    Description:  Class stub holder for Server class.

    Super-Class:

    Sub-Classes:

    Methods:
        database_names -> Stub holder for Server.conn.database_names method.

    """

    def database_names(self):

        """Function:  database_names

        Description:  Stub holder for Server.conn.database_names method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_dbs -> Test fetch_dbs method.

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
        self.doc = {"Document"}

    def test_fetch_dbs(self):

        """Function:  test_fetch_dbs

        Description:  Test fetch_dbs method.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.passwd,
                                   self.host, self.port)
        mongo.conn = FetchAdr()

        self.assertTrue(mongo.fetch_dbs())


if __name__ == "__main__":
    unittest.main()
