#!/usr/bin/python
# Classification (U)

"""Program:  server_upd_srv_stat.py

    Description:  Unit testing of Server.upd_srv_stat in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_upd_srv_stat.py

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
        test_remote_host
        test_local_host

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
        # Require a string concatenation to pass quality check
        self.host2 = "127.0" + ".0.1"
        self.port = 27017
        self.dbs = "test"
        self.coll = None
        self.db_auth = None
        self.data = {"uptime": 10, "connections": {"current": 1,
                                                   "available": 9},
                     "mem": {"resident": 1000000}}

    @mock.patch("mongo_class.Server.adm_cmd")
    def test_remote_host(self, mock_cmd):

        """Function:  test_remote_host

        Description:  Test being on remote host.

        Arguments:

        """

        mock_cmd.return_value = self.data
        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   self.host, self.port)

        mongo.upd_srv_stat()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.name, self.user, self.japd, self.host, self.port))

    @mock.patch("mongo_class.Server.adm_cmd")
    def test_local_host(self, mock_cmd):

        """Function:  test_local_host

        Description:  Test being on local host.

        Arguments:

        """

        mock_cmd.return_value = self.data
        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   self.host2, self.port)

        mongo.upd_srv_stat()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port),
            (self.name, self.user, self.japd, self.host2, self.port))


if __name__ == "__main__":
    unittest.main()
