#!/usr/bin/python
# Classification (U)

"""Program:  RepSetColl_connect.py

    Description:  Unit testing of RepSetColl.connect in mongo_class.py.

    Usage:
        test/unit/mongo_class/RepSetColl_connect.py

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
        test_no_auth -> Test with auth set to false.
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
        self.passwd = "mongo_pwd"
        self.host = "host_server"
        self.port = 27017
        self.db = "test"
        self.coll = "coll_name"
        self.db_auth = "db_name"
        self.repset = "mongo_repset"
        self.repset_hosts = "host1:27017, host2:27107"

    @mock.patch("mongo_class.pymongo.MongoClient")
    def test_no_auth(self, mock_mongo):

        """Function:  test_no_auth

        Description:  Test with auth set to false.

        Arguments:

        """

        mock_mongo.return_value = {}
        mongo = mongo_class.RepSetColl(self.name, self.user, self.passwd,
                                       self.host, self.port,
                                       repset=self.repset)
        mongo.auth = False

        self.assertFalse(mongo.connect())

    def test_no_conn_list2(self):

        """Function:  test_no_conn_list2

        Description:  Test no conn_list passed, set by repset_hosts.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(self.name, self.user, self.passwd,
                                       self.host, self.port,
                                       repset=self.repset,
                                       repset_hosts=self.repset_hosts)
        mongo.conn = True

        self.assertFalse(mongo.connect())

    def test_no_conn_list(self):

        """Function:  test_no_conn_list

        Description:  Test with no conn_list passed.

        Arguments:

        """

        mongo = mongo_class.RepSetColl(self.name, self.user, self.passwd,
                                       self.host, self.port,
                                       repset=self.repset)
        mongo.conn = True

        self.assertFalse(mongo.connect())


if __name__ == "__main__":
    unittest.main()
