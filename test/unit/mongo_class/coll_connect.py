#!/usr/bin/python
# Classification (U)

"""Program:  coll_connect.py

    Description:  Unit testing of Coll.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/coll_connect.py

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
        test_miss_coll_coll2
        test_miss_coll_coll
        test_coll_attr2
        test_coll_attr
        test_no_conn_list1
        test_no_conn_list
        test_fail_connection2
        test_fail_connection
        test_default2
        test_default

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
        self.coll = "coll_name"
        self.db_auth = None
        self.errmsg = "Error Message"
        self.errmsg2 = "Error:  Unable to connect, no collection passed."

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_miss_coll_coll2(self, mock_client, mock_cmd):

        """Function:  test_miss_coll_coll2

        Description:  Test with no Collection passed.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port)
        mongo.conn = {"test": {"coll_name": None}}

        self.assertEqual(mongo.coll_coll, None)

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_miss_coll_coll(self, mock_client, mock_cmd):

        """Function:  test_miss_coll_coll

        Description:  Test with no Collection passed.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port)
        mongo.conn = {"test": {"coll_name": None}}

        self.assertEqual(mongo.connect(), (False, self.errmsg2))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_coll_attr2(self, mock_client, mock_cmd):

        """Function:  test_coll_attr2

        Description:  Test coll attribute.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port, coll=self.coll)
        mongo.conn = {"test": {"coll_name": "connect"}}
        mongo.connect()

        self.assertEqual((mongo.coll), ("connect"))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_coll_attr(self, mock_client, mock_cmd):

        """Function:  test_coll_attr

        Description:  Test coll attribute.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port, coll=self.coll)
        mongo.conn = {"test": {"coll_name": "connect"}}

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_conn_list1(self, mock_client, mock_cmd):

        """Function:  test_no_conn_list1

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port, coll=self.coll)
        mongo.conn = {"test": {"coll_name": "connect"}}
        mongo.connect()

        self.assertEqual((mongo.coll), ("connect"))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_conn_list(self, mock_client, mock_cmd):

        """Function:  test_no_conn_list

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port, coll=self.coll)
        mongo.conn = {"test": {"coll_name": "connect"}}

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_fail_connection2(self, mock_client, mock_cmd):

        """Function:  test_fail_connection2

        Description:  Test with failed connection.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (False, self.errmsg)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port, coll=self.coll)

        self.assertEqual(mongo.coll, None)

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_fail_connection(self, mock_client, mock_cmd):

        """Function:  test_fail_connection

        Description:  Test with failed connection.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (False, self.errmsg)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port, coll=self.coll)

        self.assertEqual(mongo.connect(), (False, self.errmsg))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_default2(self, mock_client, mock_cmd):

        """Function:  test_default2

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port, coll=self.coll)
        mongo.conn = {"test": {"coll_name": "connect"}}
        mongo.connect()

        self.assertEqual((mongo.coll), ("connect"))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_default(self, mock_client, mock_cmd):

        """Function:  test_default

        Description:  Test connect method with default arguments.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)

        mongo = mongo_class.Coll(self.name, self.user, self.japd, self.host,
                                 self.port, coll=self.coll)
        mongo.conn = {"test": {"coll_name": "connect"}}

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
