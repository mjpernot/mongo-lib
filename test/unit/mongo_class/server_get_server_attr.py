#!/usr/bin/python
# Classification (U)

"""Program:  Server_get_server_attr.py

    Description:  Unit testing of Server.get_server_attr in mongo_class.py.

    Usage:
        test/unit/mongo_class/Server_get_server_attr.py

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
        test_default -> Test with default settings.

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
        self.data = {"parsed": {"storage": {"dbPath": "db_path"},
                                "systemLog": {"path": "dir_path"},
                                "config": "conf_file"}}

    @mock.patch("mongo_class.Server.upd_server_attr")
    def test_default(self, mock_cmd):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_cmd.return_value = True
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file)

        mongo.get_srv_attr()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port,
             self.conf_file))


if __name__ == "__main__":
    unittest.main()
