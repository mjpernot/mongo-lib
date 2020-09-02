#!/usr/bin/python
# Classification (U)

"""Program:  server_connect.py

    Description:  Unit testing of Server.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_connect.py

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
        test_fail_get_srv_attr -> Test with failed get_srv_attr call.
        test_auth_arg2 -> Test with auth and arg present.
        test_auth_arg -> Test with auth and arg present.
        test_auth_uri2 -> Test with auth and uri present.
        test_auth_uri -> Test with auth and uri present.
        test_no_auth2 -> Test with no auth present.
        test_no_auth -> Test with no auth present.

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
        self.conf_file = "Conf_File"
        self.use_uri = True
        self.use_arg = True

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_fail_get_srv_attr(self, mock_cmd, mock_client):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mock_cmd.return_value = (False, "Error Message")
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            use_arg=self.use_arg)

        self.assertEqual(mongo.connect(), (False, "Error Message"))
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.use_arg),
            (self.name, self.user, self.japd, self.host, self.port,
             self.use_arg))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_arg2(self, mock_cmd, mock_client):

        """Function:  test_auth_arg2

        Description:  Test with auth and arg present.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            use_arg=self.use_arg)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_arg(self, mock_cmd, mock_client):

        """Function:  test_auth_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            use_arg=self.use_arg)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.use_arg),
            (self.name, self.user, self.japd, self.host, self.port,
             self.use_arg))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_uri2(self, mock_cmd, mock_client):

        """Function:  test_auth_uri2

        Description:  Test with auth and uri present.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            use_uri=self.use_uri)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_uri(self, mock_cmd, mock_client):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            use_uri=self.use_uri)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.use_uri),
            (self.name, self.user, self.japd, self.host, self.port,
             self.use_uri))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_auth2(self, mock_cmd, mock_client):

        """Function:  test_no_auth2

        Description:  Test with no auth present.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True
        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   host=self.host, port=self.port, auth=False)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.name, self.user, self.japd, self.host, self.port))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_auth(self, mock_cmd, mock_client):

        """Function:  test_no_auth

        Description:  Test with no auth present.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True
        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   host=self.host, port=self.port, auth=False)

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
