#!/usr/bin/python
# Classification (U)

"""Program:  Rep_init.py

    Description:  Unit testing of Rep.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/Rep_init.py

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

    Super-Class:  unittest.TestCase

    Sub-Classes:

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
        self.coll = None
        self.db_auth = None
        self.repset = "mongo_repset"

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mongo = mongo_class.Rep(self.name, self.user, self.passwd, self.host,
                                self.port)

        self.assertEqual((mongo.name, mongo.user, mongo.passwd, mongo.host,
                          mongo.port),
                         (self.name, self.user, self.passwd, self.host,
                          self.port))


if __name__ == "__main__":
    unittest.main()
