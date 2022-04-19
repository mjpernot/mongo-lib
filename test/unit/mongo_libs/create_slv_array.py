#!/usr/bin/python
# Classification (U)

"""Program:  create_slv_array.py

    Description:  Unit testing of create_slv_array in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/create_slv_array.py

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
import mongo_libs
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_auth_mech
        test_no_auth_mech
        test_new_attributes
        test_create_slv_array

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = "userpd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.conf_file = "conf_file"
        self.cfg = [{"name": "name", "user": "user", "japd": "userpd",
                     "host": "host", "port": 27017, "auth": True,
                     "conf_file": "conf_file"}]
        self.cfg2 = [{"name": "name", "user": "user", "japd": "userpd",
                      "host": "host", "port": 27017, "auth": True,
                      "conf_file": "conf_file"},
                     {"name": "name", "user": "user", "japd": "userpd",
                      "host": "host", "port": 27017, "auth": True,
                      "conf_file": "conf_file", "auth_db": "admin"}]
        self.cfg3 = [{"name": "name", "user": "user", "japd": "userpd",
                      "host": "host", "port": 27017, "auth": True,
                      "conf_file": "conf_file", "mech_auth": "SCRAM-SHA-1"},
                     {"name": "name", "user": "user", "japd": "userpd",
                      "host": "host", "port": 27017, "auth": True,
                      "conf_file": "conf_file", "auth_db": "admin",
                      "mech_auth": "SCRAM-SHA-1"}]

    @mock.patch("mongo_libs.mongo_class.SlaveRep")
    def test_auth_mech(self, mock_mongo):

        """Function:  test_auth_mech

        Description:  Test with authentication mechanism passed.

        Arguments:

        """

        mock_mongo.return_value = True

        self.assertEqual(len(mongo_libs.create_slv_array(self.cfg3)), 2)

    @mock.patch("mongo_libs.mongo_class.SlaveRep")
    def test_no_auth_mech(self, mock_mongo):

        """Function:  test_no_auth_mech

        Description:  Test with no authentication mechanism passed.

        Arguments:

        """

        mock_mongo.return_value = True

        self.assertEqual(len(mongo_libs.create_slv_array(self.cfg)), 1)

    @mock.patch("mongo_libs.mongo_class.SlaveRep")
    def test_new_attributes(self, mock_mongo):

        """Function:  test_new_attributes

        Description:  Test with auth_db attributes.

        Arguments:

        """

        mock_mongo.return_value = True

        self.assertEqual(len(mongo_libs.create_slv_array(self.cfg2)), 2)

    @mock.patch("mongo_libs.mongo_class.SlaveRep")
    def test_create_slv_array(self, mock_mongo):

        """Function:  test_create_slv_array

        Description:  Test create_slv_array function.

        Arguments:

        """

        mock_mongo.return_value = True

        self.assertEqual(len(mongo_libs.create_slv_array(self.cfg)), 1)


if __name__ == "__main__":
    unittest.main()
