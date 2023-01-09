# Classification (U)

"""Program:  repset_connect.py

    Description:  Unit testing of RepSet.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/repset_connect.py

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
        test_repset
        test_fail_get_srv_attr
        test_no_repset
        test_arg
        test_auth_true2
        test_auth_true
        test_no_auth2
        test_no_auth
        test_conn_true2
        test_conn_true
        test_conn_false2
        test_conn_false
        test_connections_passed2
        test_connections_passed
        test_no_conn_list3
        test_no_conn_list2
        test_no_conn_list1
        test_no_conn_list

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
        self.repset2 = None
        self.repset_hosts = "host1:27017, host2:27107"
        self.db_auth = None
        self.conf_file = "Conf_File"
        self.connections = ["mongo1:27017", "mongo2:27017", "mongo3:27017"]
        self.conn = "Mongo_Connection"
        self.errmsg = "Error Message"

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_repset(self, mock_get, mock_mongo):

        """Function:  test_repset

        Description:  Test with repset present.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_fail_get_srv_attr(self, mock_get, mock_mongo):

        """Function:  test_fail_get_srv_attr

        Description:  Test with failed get_srv_attr call.

        Arguments:

        """

        mock_get.return_value = (False, self.errmsg)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)

        self.assertEqual(mongo.connect(), (False, self.errmsg))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_repset(self, mock_get, mock_mongo):

        """Function:  test_no_repset

        Description:  Test with no repset present.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset2, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_arg(self, mock_get, mock_mongo):

        """Function:  test_arg

        Description:  Test with arg present.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_true2(self, mock_get, mock_mongo):

        """Function:  test_auth_true2

        Description:  Test with auth set to True.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)
        mongo.connect()

        self.assertTrue(mongo.auth)

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_auth_true(self, mock_get, mock_mongo):

        """Function:  test_auth_true

        Description:  Test with auth set to True.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_auth2(self, mock_get, mock_mongo):

        """Function:  test_no_auth2

        Description:  Test with no authenication set.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)
        mongo.connect()

        self.assertFalse(mongo.auth)

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_auth(self, mock_get, mock_mongo):

        """Function:  test_no_auth

        Description:  Test with no authenication set.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=False)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_true2(self, mock_get, mock_mongo):

        """Function:  test_conn_true2

        Description:  Test with conn set to true.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)
        mongo.connect()

        self.assertTrue(mongo.auth)

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_true(self, mock_get, mock_mongo):

        """Function:  test_conn_true

        Description:  Test with conn set to true.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(
            self.name, self.user, self.japd, self.host, self.port,
            repset=self.repset, auth=True)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_false2(self, mock_get, mock_mongo):

        """Function:  test_conn_false2

        Description:  Test with conn set to false.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)
        mongo.connect()

        self.assertEqual(mongo.conn, self.conn)

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_false(self, mock_get, mock_mongo):

        """Function:  test_conn_false

        Description:  Test with conn set to false.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mock_mongo.return_value = self.conn

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_connections_passed2(self, mock_get):

        """Function:  test_connections_passed2

        Description:  Test with connections passed.

        Arguments:

        """

        mock_get.return_value = (True, None)

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)
        mongo.conn = True
        mongo.connect(connections=self.connections)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_connections_passed(self, mock_get):

        """Function:  test_connections_passed

        Description:  Test with connections passed.

        Arguments:

        """

        mock_get.return_value = (True, None)

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)
        mongo.conn = True

        self.assertEqual(mongo.connect(connections=self.connections),
                         (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_conn_list3(self, mock_get):

        """Function:  test_no_conn_list3

        Description:  Test no connections passed, set by repset_hosts.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset,
                                   repset_hosts=self.repset_hosts)
        mongo.conn = True
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             self.repset_hosts))

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_conn_list2(self, mock_get):

        """Function:  test_no_conn_list2

        Description:  Test no connections passed, set by repset_hosts.

        Arguments:

        """

        mock_get.return_value = (True, None)
        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset,
                                   repset_hosts=self.repset_hosts)
        mongo.conn = True

        self.assertEqual(mongo.connect(), (True, None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_conn_list1(self, mock_get):

        """Function:  test_no_conn_list2

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_get.return_value = (True, None)

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)
        mongo.conn = True
        mongo.connect()

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.repset_hosts),
            (self.name, self.user, self.japd, self.host, self.port,
             None))

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_conn_list(self, mock_get):

        """Function:  test_no_conn_list

        Description:  Test with no connections passed.

        Arguments:

        """

        mock_get.return_value = (True, None)

        mongo = mongo_class.RepSet(self.name, self.user, self.japd,
                                   self.host, self.port, repset=self.repset)
        mongo.conn = True

        self.assertEqual(mongo.connect(), (True, None))


if __name__ == "__main__":
    unittest.main()
