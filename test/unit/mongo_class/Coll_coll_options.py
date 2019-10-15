#!/usr/bin/python
# Classification (U)

"""Program:  Coll_coll_options.py

    Description:  Unit testing of Coll.coll_options in mongo_class.py.

    Usage:
        test/unit/mongo_class/Coll_coll_options.py

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


class CollOpts(object):

    """Class:  CollOpts

    Description:  Class stub holder for Coll class.

    Methods:
        options -> Stub for Coll.coll_options method.

    """

    def options(self):

        """Function:  options

        Description:  Stub for Coll.coll_options method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_query -> Test method.

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
        self.coll = "coll_name"
        self.db_auth = None

    def test_query(self):

        """Function:  test_query

        Description:  Test method.

        Arguments:

        """

        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port)
        mongo.coll = CollOpts()

        self.assertTrue(mongo.coll_options())


if __name__ == "__main__":
    unittest.main()
