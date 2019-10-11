#!/usr/bin/python
# Classification (U)

"""Program:  create_instance.py

    Description:  Unit testing of create_instance in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/create_instance.py

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

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, name, user, passwd, host, port, **kwargs):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.auth = kwargs.get("auth", None)
        self.conf_file = kwargs.get("conf_file", None)


class Cfg(object):

    """Class:  Cfg

    Description:  Class stub holder for Cfg class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.passwd = "passwd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.conf_file = "conf_file"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_create_instance -> Test create_instance function.

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

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_create_instance(self, mock_load):

        """Function:  test_create_instance

        Description:  Test create_instance function.

        Arguments:

        """

        mock_load.return_value = Cfg()
        mongo = mongo_libs.create_instance("cfg_file", "dir_path", Mongo)
        self.assertEqual((mongo.name, mongo.user, mongo.passwd, mongo.host,
                          mongo.port, mongo.auth, mongo.conf_file),
                         (self.name, self.user, self.passwd, self.host,
                          self.port, self.auth, self.conf_file))


if __name__ == "__main__":
    unittest.main()
