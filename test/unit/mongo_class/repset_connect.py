#!/usr/bin/python
# Classification (U)

"""Program:  RepSet_connect.py

    Description:  Unit testing of RepSet.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/RepSet_connect.py

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
        test_no_auth -> Test with no authenication set.
        test_conn_true -> Test with conn set to true.
        test_conn_false -> Test with conn set to false.
        test_connections_passed -> Test with connections passed.
        test_no_conn_list2 -> Test no connections passed, set by repset_hosts.
        test_no_conn_list -> Test with no connections passed.

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
        self.repset = "mongo_repset"
        self.repset_hosts = "host1:27017, host2:27107"
        self.db_auth = None
        self.conf_file = "Conf_File"
        self.use_uri = True
        self.use_arg = True
        self.connections = ["mongo1:27017", "mongo2:27017", "mongo3:27017"]
        self.conn = "Mongo_Connection"

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_arg(self, mock_get, mock_mongo):

        """Function:  test_auth_arg

        Description:  Test with auth and arg present.

        Arguments:

        """

        mock_get.return_value = True
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True, use_arg=True)
        mongo.connect()

        self.assertTrue(mongo.use_arg)

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_uri(self, mock_get, mock_mongo):

        """Function:  test_auth_uri

        Description:  Test with auth and uri present.

        Arguments:

        """

        mock_get.return_value = True
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True, use_uri=True)
        mongo.connect()

        self.assertTrue(mongo.use_uri)

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_auth(self, mock_get, mock_mongo):

        """Function:  test_no_auth

        Description:  Test with no authenication set.

        Arguments:

        """

        mock_get.return_value = True
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)
        mongo.connect()

        self.assertFalse(mongo.auth)

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_true(self, mock_get, mock_mongo):

        """Function:  test_conn_true

        Description:  Test with conn set to true.

        Arguments:

        """

        mock_get.return_value = True
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)
        mongo.connect()

        self.assertTrue(mongo.auth)

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_false(self, mock_get, mock_mongo):

        """Function:  test_conn_false

        Description:  Test with conn set to false.

        Arguments:

        """

        mock_get.return_value = True
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)
        mongo.connect()

        self.assertEqual(mongo.conn, self.conn)

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_connections_passed(self, mock_get):

        """Function:  test_connections_passed

        Description:  Test with connections passed.

        Arguments:

        """

        mock_get.return_value = True

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)
        mongo.connect(connections=self.connections)
        mongo.conn = True

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_conn_list2(self, mock_get):

        """Function:  test_no_conn_list2

        Description:  Test no connections passed, set by repset_hosts.

        Arguments:

        """

        mock_get.return_value = True
        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset,
                                   repset_hosts=self.repset_hosts)
        mongo.connect()
        mongo.conn = True

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             self.repset_hosts))

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_conn_list(self, mock_get):

        """Function:  test_no_conn_list

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_get.return_value = True

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)
        mongo.connect()
        mongo.conn = True

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             None))


if __name__ == "__main__":
    unittest.main()
