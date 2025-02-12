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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_class                              # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class DBConn():                                 # pylint:disable=R0903

    """Class:  DBConn

    Description:  Class stub holder for DB class.

    Methods:
        __init__

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
        setUp
        test_db_attr2
        test_db_attr
        test_no_conn_list1
        test_no_conn_list
        test_fail_connection2
        test_fail_connection
        test_connection2
        test_connection

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

        self.assertEqual(mongo.db_inst, "testdb")

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

        self.assertEqual(mongo.db_inst, "testdb")

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

        self.assertIsNone(mongo.db_inst)

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

        self.assertEqual(mongo.db_inst, "testdb")


if __name__ == "__main__":
    unittest.main()
