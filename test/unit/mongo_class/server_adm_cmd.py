#!/usr/bin/python
# Classification (U)

"""Program:  server_adm_cmd.py

    Description:  Unit testing of Server.adm_cmd in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_adm_cmd.py

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


class Command1(object):

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
        self.arg1 = None

    def command(self, cmd, arg1):

        """Function:  database_names

        Description:  Stub holder for Server.conn.database_names method.

        Arguments:

        """

        self.cmd = cmd
        self.arg1 = arg1

        return True


class Admin1(object):

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
        test_arg
        test_adm_cmd

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
        self.doc = {"Document"}
        self.cmd = "Command"
        self.arg1 = "Argument"

    def test_arg(self):

        """Function:  test_arg

        Description:  Test with argument passed.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   self.host, self.port)
        mongo.conn = Admin1()

        self.assertTrue(mongo.adm_cmd(self.cmd, arg1=self.arg1))

    def test_adm_cmd(self):

        """Function:  test_adm_cmd

        Description:  Test adm_cmd method.

        Arguments:

        """

        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   self.host, self.port)
        mongo.conn = Admin1()

        self.assertTrue(mongo.adm_cmd(self.cmd))


if __name__ == "__main__":
    unittest.main()
