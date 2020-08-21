#!/usr/bin/python
# Classification (U)

"""Program:  crt_coll_inst.py

    Description:  Unit testing of crt_coll_inst in mongo_libs.py.

    Usage:
        test/unit/mongo_libs/crt_coll_inst.py

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


class Cfg(object):

    """Class:  Cfg

    Description:  Class stub holder for Cfg class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, repset_hosts=None):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japwd = None
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.repset = "repset_name"
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"


class Cfg2(object):

    """Class:  Cfg2

    Description:  Class stub holder for Cfg class with new attributes.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, repset_hosts=None):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japwd = None
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.repset = "repset_name"
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"
        self.use_uri = False
        self.use_arg = True
        self.auth_db = "mydatabase"


class CfgA(object):

    """Class:  Cfg

    Description:  Class stub holder for Cfg class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, repset_hosts=None):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = "usrpd"
        self.host = "host"
        self.port = 27017
        self.auth = True
        self.repset = "repset_name"
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_coll_new_attrs2 -> Test new use_uri, use_arg, & auth_db attrs.
        test_repsetcoll_new_attrs2 -> Test new use_uri, use_arg, auth_db attr.
        test_coll_new_attrs -> Test with new use_uri, use_arg, & auth_db attrs.
        test_repsetcoll_new_attrs -> Test new use_uri, use_arg, & auth_db attr.
        test_coll -> Test the mongo_class.Coll class.
        test_repsetcoll -> Test the mongo_class.RepSetColl class.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.repset_hosts = "host:port"

    @mock.patch("mongo_libs.mongo_class.Coll")
    def test_coll_new_attrs2(self, mock_mongo):

        """Function:  test_coll_new_attrs2

        Description:  Test with new use_uri, use_arg, and auth_db attrs.

        Arguments:

        """

        cfg = Cfg2()
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

    @mock.patch("mongo_libs.mongo_class.RepSetColl")
    def test_repsetcoll_new_attrs2(self, mock_mongo):

        """Function:  test_repsetcoll_new_attrs2

        Description:  Test with new use_uri, use_arg, and auth_db attrs.

        Arguments:

        """

        cfg = Cfg2(self.repset_hosts)
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

    @mock.patch("mongo_libs.mongo_class.Coll")
    def test_coll_new_attrs(self, mock_mongo):

        """Function:  test_coll_new_attrs

        Description:  Test with new use_uri, use_arg, and auth_db attrs.

        Arguments:

        """

        cfg = Cfg()
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

    @mock.patch("mongo_libs.mongo_class.RepSetColl")
    def test_repsetcoll_new_attrs(self, mock_mongo):

        """Function:  test_repsetcoll_new_attrs

        Description:  Test with new use_uri, use_arg, and auth_db attrs.

        Arguments:

        """

        cfg = Cfg(self.repset_hosts)
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

    @mock.patch("mongo_libs.mongo_class.Coll")
    def test_coll(self, mock_mongo):

        """Function:  test_coll

        Description:  Test the mongo_class.Coll class.

        Arguments:

        """

        cfg = Cfg()
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

    @mock.patch("mongo_libs.mongo_class.RepSetColl")
    def test_repsetcoll(self, mock_mongo):

        """Function:  test_repsetcoll

        Description:  Test the mongo_class.RepSetColl class.

        Arguments:

        """

        cfg = Cfg(self.repset_hosts)
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))


if __name__ == "__main__":
    unittest.main()
