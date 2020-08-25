#!/usr/bin/python
# Classification (U)

"""Program:  server_upd_server_attr.py

    Description:  Unit testing of Server.upd_server_attr in mongo_class.py.

    Usage:
        test/unit/mongo_class/server_upd_server_attr.py

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
        test_no_conf_file -> Test with no conf_file present.
        test_conf_file -> Test with conf_file present.

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

    @mock.patch("mongo_class.Server.adm_cmd")
    def test_no_conf_file(self, mock_cmd):

        """Function:  test_no_conf_file

        Description:  Test with no conf_file present.

        Arguments:

        """

        mock_cmd.return_value = self.data
        mongo = mongo_class.Server(self.name, self.user, self.japd,
                                   self.host, self.port)

        mongo.upd_server_attr()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port,
             "conf_file"))

    @mock.patch("mongo_class.fetch_cmd_line")
    def test_conf_file(self, mock_cmd):

        """Function:  test_conf_file

        Description:  Test with conf_file present.

        Arguments:

        """

        mock_cmd.return_value = self.data
        mongo = mongo_class.Server(
            self.name, self.user, self.japd, self.host, self.port,
            conf_file=self.conf_file)

        mongo.upd_server_attr()
        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port,
             self.conf_file))


if __name__ == "__main__":
    unittest.main()
