#!/usr/bin/python
# Classification (U)

"""Program:  Coll_init.py

    Description:  Unit testing of Coll.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/Coll_init.py

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
        self.dbs = "test"
        self.coll = "coll_name"
        self.db_auth = None

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port, coll=self.coll)

        self.assertEqual((mongo.name, mongo.user, mongo.passwd, mongo.host,
                          mongo.port, mongo.coll_db, mongo.coll_coll),
                         (self.name, self.user, self.passwd, self.host,
                          self.port, self.dbs, self.coll))


if __name__ == "__main__":
    unittest.main()
