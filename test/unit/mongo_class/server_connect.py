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
        setUp
        test_auth_mech3
        test_auth_mech2
        test_auth_mech
        test_conn_false2
        test_conn_false
        test_conn_true2
        test_conn_true
        test_fail_get_srv_attr2
        test_fail_get_srv_attr
        test_auth_arg4
        test_auth_arg3
        test_auth_arg2
        test_auth_arg
        test_no_auth2
        test_no_auth

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
        self.errmsg = "Error Message"
        self.auth_mech = "SCRAM-SHA-1"
        self.auth_mech2 = "MONGODB-CR"

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_mech3(self, mock_cmd, mock_client):

        """Function:  test_auth_mech3

        Description:  Test with auth_mech set to SCRAM-SHA-1.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=True, use_arg=True, auth_mech=self.auth_mech)
        mongo.conn = False
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth_mech),
            (self.name, self.user, self.japd, self.host, self.port,
             self.auth_mech))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_mech2(self, mock_cmd, mock_client):

        """Function:  test_auth_mech2

        Description:  Test with auth_mech set to MONGODB-CR.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=True, use_arg=True, auth_mech=self.auth_mech2)
        mongo.conn = False
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth_mech),
            (self.name, self.user, self.japd, self.host, self.port,
             self.auth_mech2))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_mech(self, mock_cmd, mock_client):

        """Function:  test_auth_mech

        Description:  Test with auth_mech default.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=True, use_arg=True)
        mongo.conn = False
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth_mech),
            (self.name, self.user, self.japd, self.host, self.port,
             self.auth_mech))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_false2(self, mock_cmd, mock_client):

        """Function:  test_conn_false2

        Description:  Test with conn set to False.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=True, use_arg=True)
        mongo.conn = False
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.name, self.user, self.japd, self.host, self.port))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_false(self, mock_cmd, mock_client):

        """Function:  test_conn_false

        Description:  Test with conn set to False.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=True, use_arg=True)
        mongo.conn = False

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_true2(self, mock_cmd, mock_client):

        """Function:  test_conn_true2

        Description:  Test with conn set to True.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=True, use_arg=True)
        mongo.conn = True
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.name, self.user, self.japd, self.host, self.port))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_true(self, mock_cmd, mock_client):

        """Function:  test_conn_true

        Description:  Test with conn set to True.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True

        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=True, use_arg=True)
        mongo.conn = True

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_fail_get_srv_attr2(self, mock_cmd, mock_client):

        """Function:  test_fail_get_srv_attr2

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mock_cmd.return_value = (False, self.errmsg)
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.name, self.user, self.japd, self.host, self.port))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_fail_get_srv_attr(self, mock_cmd, mock_client):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mock_cmd.return_value = (False, self.errmsg)
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port)

        self.assertEqual(mongo.connect(), (False, self.errmsg))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_arg4(self, mock_cmd, mock_client):

        """Function:  test_auth_arg4

        Description:  Test with arg present and no auth.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=False)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_arg3(self, mock_cmd, mock_client):

        """Function:  test_auth_arg3

        Description:  Test with arg present and no auth.

        Arguments:

        """

        mock_cmd.return_value = (True, None)
        mock_client.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, host=self.host, port=self.port,
            auth=False)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.name, self.user, self.japd, self.host, self.port))

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
            self.name, self.user, self.japd, host=self.host, port=self.port)

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
            self.name, self.user, self.japd, host=self.host, port=self.port)
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.name, self.user, self.japd, self.host, self.port))

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
        mongo.connect()

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
