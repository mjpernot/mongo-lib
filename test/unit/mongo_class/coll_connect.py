#!/usr/bin/python
# Classification (U)

"""Program:  Coll_connect.py

    Description:  Unit testing of Coll.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/Coll_connect.py

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

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_default(self, mock_client, mock_cmd):

        """Function:  test_default

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = True
        mongo = mongo_class.Coll(self.name, self.user, self.passwd,
                                 self.host, self.port, coll=self.coll)
        mongo.conn = {"test": {"coll_name": "connect"}}
        mongo.connect()

        self.assertEqual((mongo.coll), ("connect"))


if __name__ == "__main__":
    unittest.main()
