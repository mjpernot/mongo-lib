#!/usr/bin/python
# Classification (U)

"""Program:  Server_fetch_adr.py

    Description:  Unit testing of Server.fetch_adr in mongo_class.py.

    Usage:
        test/unit/mongo_class/Server_fetch_adr.py

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


class Conn(object):

    """Class:  Conn

    Description:  Class stub holder for Rep class.

    Methods:
        __init__ -> Stub holder for Rep.conn method.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for Rep.conn.fetch_adr attribute.

        Arguments:

        """

        self.address = True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_adr -> Test fetch_adr method.

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
        self.coll = None
        self.db_auth = None

    def test_fetch_adr(self):

        """Function:  test_fetch_adr

        Description:  Test fetch_adr method.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japwd, self.host,
                                self.port)
        mongo.conn = Conn()

        self.assertEqual(mongo.fetch_adr(), True)


if __name__ == "__main__":
    unittest.main()
