#!/usr/bin/python
# Classification (U)

"""Program:  DB_db_cmd.py

    Description:  Unit testing of DB.db_cmd in mongo_class.py.

    Usage:
        test/unit/mongo_class/DB_db_cmd.py

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


class DBValidate(object):

    """Class:  DBValidate

    Description:  Class stub holder for DB class.

    Methods:
        command -> Stub for DB.db.command method.

    """

    def command(self, cmd, **kwargs):

        """Function:  command

        Description:  Stub for DB.db.command method.

        Arguments:
            (input) cmd -> Database command.
            (input) **kwargs:
                obj -> Name of object command will work against.
            (output) Returns the output of the database command.

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_default -> Test with minimum number of arguments.

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
        self.db_auth = None

    def test_default(self):

        """Function:  test_default

        Description:  Test db_cmd method with default arguments.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.passwd,
                               self.host, self.port)
        mongo.db = DBValidate()

        self.assertTrue(mongo.db_cmd("command", obj="object_name"))


if __name__ == "__main__":
    unittest.main()
