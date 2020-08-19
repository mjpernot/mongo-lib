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
        test_no_auth -> Test with no authenication set.
        test_conn_true -> Test with conn set to true.
        test_conn_false -> Test with conn set to false.
        test_no_conn_list2 -> Test no conn_list passed, set by repset_hosts.
        test_no_conn_list -> Test with no conn_list passed.

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
        self.db_auth = False
        self.repset = "mongo_repset"
        self.repset_hosts = "host1:27017, host2:27107"

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_auth(self, mock_get, mock_mongo):

        """Function:  test_no_auth

        Description:  Test with no authenication set.

        Arguments:

        """

        mock_get.return_value = True
        mock_mongo.return_value = True
        mongo = mongo_class.RepSet(self.name, self.user, self.japwd,
                                   self.host, self.port, repset=self.repset)
        mongo.auth = False

        self.assertFalse(mongo.connect())

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_true(self, mock_get, mock_mongo):

        """Function:  test_conn_true

        Description:  Test with conn set to true.

        Arguments:

        """

        mock_get.return_value = True
        mock_mongo.return_value = True
        mongo = mongo_class.RepSet(self.name, self.user, self.japwd,
                                   self.host, self.port, repset=self.repset)
        mongo.auth = True

        self.assertFalse(mongo.connect())

    @mock.patch("mongo_class.pymongo.MongoClient")
    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_conn_false(self, mock_get, mock_mongo):

        """Function:  test_conn_false

        Description:  Test with conn set to false.

        Arguments:

        """

        mock_get.return_value = True
        mock_mongo.return_value = True
        mongo = mongo_class.RepSet(self.name, self.user, self.japwd,
                                   self.host, self.port, repset=self.repset)

        self.assertFalse(mongo.connect())

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_conn_list2(self, mock_get):

        """Function:  test_no_conn_list2

        Description:  Test no conn_list passed, set by repset_hosts.

        Arguments:

        """

        mock_get.return_value = True
        mongo = mongo_class.RepSet(self.name, self.user, self.japwd,
                                   self.host, self.port, repset=self.repset,
                                   repset_hosts=self.repset_hosts)
        mongo.conn = True

        self.assertFalse(mongo.connect())

    @mock.patch("mongo_class.Server.get_srv_attr")
    def test_no_conn_list(self, mock_get):

        """Function:  test_no_conn_list

        Description:  Test with no conn_list passed.

        Arguments:

        """

        mock_get.return_value = True
        mongo = mongo_class.RepSet(self.name, self.user, self.japwd,
                                   self.host, self.port, repset=self.repset)
        mongo.conn = True

        self.assertFalse(mongo.connect())


if __name__ == "__main__":
    unittest.main()
