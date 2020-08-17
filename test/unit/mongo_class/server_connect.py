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
        test_auth_arg -> Test with auth and arg present.
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
        self.coll = None
        self.db_auth = None
        self.conf_file = "Conf_File"
        self.use_uri = True
        self.use_arg = True

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_arg(self, mock_cmd, mock_client):

        """Function:  test_auth_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mock_cmd.return_value = True
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japwd, host=self.host, port=self.port,
            use_arg=self.use_arg)

        mongo.connect()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japwd, mongo.host, mongo.port,
             mongo.use_arg),
            (self.name, self.user, self.japwd, self.host, self.port,
             self.use_arg))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_uri(self, mock_cmd, mock_client):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mock_cmd.return_value = True
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japwd, host=self.host, port=self.port,
            use_uri=self.use_uri)

        mongo.connect()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japwd, mongo.host, mongo.port,
             mongo.use_uri),
            (self.name, self.user, self.japwd, self.host, self.port,
             self.use_uri))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_auth(self, mock_cmd, mock_client):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mock_cmd.return_value = True
        mock_client.return_value = True
        mongo = mongo_class.Server(self.name, self.user, self.japwd,
                                   host=self.host, port=self.port, auth=False)

        mongo.connect()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japwd, mongo.host, mongo.port),
            (self.name, self.user, self.japwd, self.host, self.port))


if __name__ == "__main__":
    unittest.main()
