#!/usr/bin/python
# Classification (U)

"""Program:  SlaveRep_init.py

    Description:  Unit testing of SlaveRep.__init__ in mongo_class.py.

    Usage:
        test/unit/mongo_class/SlaveRep_init.py

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
import mock

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
        self.data = {"secondary": True, "ismaster": False,
                     "issecondary": True, "setName": "mongo_repset",
                     "primary": "primary_host"}

    @mock.patch("mongo_class.fetch_ismaster")
    @mock.patch("mongo_class.Server.connect")
    def test_default(self, mock_connect, mock_fetch):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mock_connect.return_value = True
        mock_fetch.return_value = self.data
        mongo = mongo_class.SlaveRep(self.name, self.user, self.passwd,
                                     self.host, self.port, repset=self.repset)

        self.assertEqual((mongo.name, mongo.user, mongo.passwd, mongo.host,
                          mongo.port, mongo.db, mongo.coll, mongo.repset,
                          mongo.ismaster, mongo.issecondary),
                         (self.name, self.user, self.passwd, self.host,
                          self.port, self.db, self.coll, self.repset, False,
                          True))


if __name__ == "__main__":
    unittest.main()
