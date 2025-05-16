# Classification (U)

"""Program:  server_unlock_db.py

    Description:  Unit testing of Server.unlock_db in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_unlock_db.py

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
        test_unlock_db

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

    def test_unlock_db(self):

        """Function:  test_unlock_db

        Description:  Test unlock_db method.

        Arguments:

        """

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port)
        mongo.conn = Admin1()

        self.assertFalse(mongo.unlock_db())


if __name__ == "__main__":
    unittest.main()
