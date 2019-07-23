#!/usr/bin/python
# Classification (U)

"""Program:  Server_fetch_svr_info.py

    Description:  Unit testing of Server.fetch_svr_info in mongo_class.py.

    Usage:
        test/unit/mongo_class/Server_fetch_svr_info.py

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


class ServerInfo(object):

    """Class:  ServerInfo

    Description:  Class stub holder for Server class.

    Super-Class:

    Sub-Classes:

    Methods:
        server_info -> Stub holder for Server.conn.server_info method.

    """

    def server_info(self):

        """Function:  database_names

        Description:  Stub holder for Server.conn.server_info method.

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
        test_fetch_svr_info -> Test fetch_svr_info method.

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

    def test_fetch_svr_info(self):

        """Function:  test_fetch_svr_info

        Description:  Test fetch_svr_info method.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.passwd,
                                   self.host, self.port)
        mongo.conn = ServerInfo()

        self.assertTrue(mongo.fetch_svr_info())


if __name__ == "__main__":
    unittest.main()
