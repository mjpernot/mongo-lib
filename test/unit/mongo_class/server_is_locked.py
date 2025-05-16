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
import mongo_class                              # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Command1():                                       # pylint:disable=R0903

    """Class:  Command1

    Description:  Class stub holder for command class.

    Methods:
        __init__
        command

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class.

        Arguments:

        """

        self.cmd = None
        self.data = {"fsyncLock": True}

    def command(self, cmd):

        """Function:  database_names

        Description:  Stub holder for Server.conn.database_names method.

        Arguments:

        """

        self.cmd = cmd

        return self.data


class Admin1():                                         # pylint:disable=R0903

    """Class:  Admin1

    Description:  Class stub holder for admin class.

    Methods:
        __init__

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialization of class.

        Arguments:

        """

        self.admin = Command1()


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

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port)
        mongo.conn = Admin1()

        self.assertTrue(mongo.is_locked())


if __name__ == "__main__":
    unittest.main()
