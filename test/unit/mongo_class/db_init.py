#!/usr/bin/python
# Classification (U)

"""Program:  DB_init.py

    Description:  Unit testing of DB.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/DB_init.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_auth_uri -> Test with auth and uri present.
        test_no_auth -> Test with no auth present.

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
        self.db_auth = None

    def test_auth_uri(self):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japwd,
                               self.host, self.port)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japwd, mongo.host, mongo.port),
            (self.name, self.user, self.japwd, self.host, self.port))

    def test_no_auth(self):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mongo = mongo_class.DB(self.name, self.user, self.japwd,
                               self.host, self.port)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japwd, mongo.host, mongo.port),
            (self.name, self.user, self.japwd, self.host, self.port))


if __name__ == "__main__":
    unittest.main()
