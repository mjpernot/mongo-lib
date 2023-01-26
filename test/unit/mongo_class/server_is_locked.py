# Classification (U)

"""Program:  server_is_locked.py

    Description:  Unit testing of Server.is_locked in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_is_locked.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest

# Local
sys.path.append(os.getcwd())
import mongo_class
import version

__version__ = version.__version__


class Conn(object):

    """Class:  Conn

    Description:  Class stub holder for Rep class.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Stub holder for Rep.conn.is_locked attribute.

        Arguments:

        """

        self.is_locked = True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_is_locked

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mongo_Server"
        self.user = "mongo_user"
        self.japd = "mongo_pd"
        self.host = "host_server"
        self.port = 27017
        self.dbs = "test"
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"
        self.nodes = ["node1", "node2"]

    def test_is_locked(self):

        """Function:  test_is_locked

        Description:  Test is_locked method.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.japd, self.host,
                                self.port)
        mongo.conn = Conn()

        self.assertEqual(mongo.is_locked(), True)


if __name__ == "__main__":
    unittest.main()
