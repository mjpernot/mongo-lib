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


class Mongo(object):

    """Class:  Mongo

    Description:  Class stub holder for Mongo class.

    Super-Class:

    Sub-Classes:

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, name, user, passwd, host, port, auth, conf_file):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.auth = auth
        self.conf_file = conf_file


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Super-Class:  unittest.TestCase

    Sub-Classes:

    Methods:
        setUp -> Initialize testing environment.
        test_create_slv_array -> Test create_slv_array function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.passwd = "passwd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.conf_file = "conf_file"
        self.cfg = [{"name": "name", "user": "user", "passwd": "passwd",
                     "host": "host", "port": 27017, "auth": True,
                     "conf_file": "conf_file"}]

    @mock.patch("mongo_libs.mongo_class.SlaveRep")
    def test_create_slv_array(self, mock_mongo):

        """Function:  test_create_slv_array

        Description:  Test create_slv_array function.

        Arguments:

        """

        mock_mongo.return_value = Mongo

        self.assertEqual(len(mongo_libs.create_slv_array(self.cfg)), 1)


if __name__ == "__main__":
    unittest.main()
