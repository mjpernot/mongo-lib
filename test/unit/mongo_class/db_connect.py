#!/usr/bin/python
# Classification (U)

"""Program:  db_connect.py

    Description:  Unit testing of DB.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/db_connect.py

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


class DBConn(object):

    """Class:  DBConn

    Description:  Class stub holder for DB class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.test = "testdb"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_db_attr2 -> Test db attribute.
        test_db_attr -> Test db attribute.
        test_no_conn_list1 -> Test with no connections passed.
        test_no_conn_list -> Test with no connections passed.
        test_fail_connection2 -> Test with failed connection.
        test_fail_connection -> Test with failed connection.
        test_connection2 -> Test connection method.
        test_connection -> Test connection method.

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
        self.db_auth = None
        self.errmsg = "Error Message"

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_db_attr2(self, mock_client, mock_cmd):

        """Function:  test_db_attr2

        Description:  Test db attribute.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)
        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.conn = {"test": "testdb"}

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_db_attr(self, mock_client, mock_cmd):

        """Function:  test_db_attr

        Description:  Test db attribute.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)
        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.conn = {"test": "testdb"}
        mongo.connect()

        self.assertEqual(mongo.db, "testdb")

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_conn_list1(self, mock_client, mock_cmd):

        """Function:  test_no_conn_list1

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)
        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.conn = {"test": "testdb"}

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_conn_list(self, mock_client, mock_cmd):

        """Function:  test_no_conn_list

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)
        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.conn = {"test": "testdb"}
        mongo.connect()

        self.assertEqual(mongo.db, "testdb")

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_fail_connection2(self, mock_client, mock_cmd):

        """Function:  test_fail_connection2

        Description:  Test with failed connection.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (False, self.errmsg)
        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)

        self.assertEqual((mongo.db), (None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_fail_connection(self, mock_client, mock_cmd):

        """Function:  test_fail_connection

        Description:  Test with failed connection.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (False, self.errmsg)
        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)

        self.assertEqual(mongo.connect(), (False, self.errmsg))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_connection2(self, mock_client, mock_cmd):

        """Function:  test_connection2

        Description:  Test connection method.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)
        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.conn = {"test": "testdb"}

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_connection(self, mock_client, mock_cmd):

        """Function:  test_connection

        Description:  Test connection method.

        Arguments:

        """

        mock_client.return_value = True
        mock_cmd.return_value = (True, None)
        mongo = mongo_class.DB(self.name, self.user, self.japd,
                               self.host, self.port)
        mongo.conn = {"test": "testdb"}
        mongo.connect()

        self.assertEqual((mongo.db), ("testdb"))


if __name__ == "__main__":
    unittest.main()
