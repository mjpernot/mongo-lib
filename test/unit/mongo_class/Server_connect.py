#!/usr/bin/python
# Classification (U)

"""Program:  Server_connect.py

    Description:  Unit testing of Server.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/Server_connect.py

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
        test_no_auth -> Test with no auth present.
        test_auth -> Test with auth present.

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
        self.conf_file = "Conf_File"

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.adm_cmd")
    def test_no_auth(self, mock_cmd, mock_client):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mock_cmd.return_value = True
        mock_cmd.return_value = self.data
        mongo = mongo_class.Server(self.name, self.user, self.passwd,
                                   self.host, self.port, auth=False)

        mongo.connect()
        self.assertEqual((mongo.name, mongo.user, mongo.passwd, mongo.host,
                          mongo.port, mongo.db),
                         (self.name, self.user, self.passwd, self.host,
                          self.port, self.db))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth(self, mock_cmd, mock_client):

        """Function:  test_auth

        Description:  Test with auth present.

        Arguments:

        """

        mock_cmd.return_value = True
        mock_client.return_value = True
        mongo = mongo_class.Server(self.name, self.user, self.passwd,
                                   self.host, self.port)

        mongo.connect()
        self.assertEqual((mongo.name, mongo.user, mongo.passwd, mongo.host,
                          mongo.port, mongo.db),
                         (self.name, self.user, self.passwd, self.host,
                          self.port, self.db))


if __name__ == "__main__":
    unittest.main()
