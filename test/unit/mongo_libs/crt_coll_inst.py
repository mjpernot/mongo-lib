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
        __init__

    """

    def __init__(self, repset_hosts=None):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = "userpd"
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
        __init__

    """

    def __init__(self, repset_hosts=None):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = "userpd"
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
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None


class Cfg3(object):

    """Class:  Cfg3

    Description:  Class stub holder for Cfg class with new attributes.

    Methods:
        __init__

    """

    def __init__(self, repset_hosts=None):

        """Function:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.user = "user"
        self.japd = "userpd"
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
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_coll_set_ssl
        test_rep_set_ssl
        test_coll_none_ssl
        test_rep_none_ssl
        test_coll_no_ssl
        test_rep_no_ssl
        test_coll_mech_auth
        test_coll_no_mech_auth
        test_repset_mech_auth
        test_repset_no_mech_auth
        test_coll_new_attrs2
        test_repsetcoll_new_attrs2
        test_coll_new_attrs
        test_repsetcoll_new_attrs
        test_coll
        test_repsetcoll

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.repset_hosts = "host:port"

    def test_coll_set_ssl(self):

        """Function:  test_coll_set_ssl

        Description:  Test mongo_class.Coll class with SSL set.

        Arguments:

        """

        cfg = Cfg3()
        mongo = mongo_libs.crt_coll_inst(cfg, "db", "tbl")

        self.assertEqual(mongo.ssl_client_ca, cfg.ssl_client_ca)

    def test_rep_set_ssl(self):

        """Function:  test_rep_set_ssl

        Description:  Test mongo_class.RepSetColl class with SSL set.

        Arguments:

        """

        cfg = Cfg3(self.repset_hosts)
        mongo = mongo_libs.crt_coll_inst(cfg, "db", "tbl")

        self.assertEqual(mongo.ssl_client_ca, cfg.ssl_client_ca)

    def test_coll_none_ssl(self):

        """Function:  test_coll_none_ssl

        Description:  Test mongo_class.Coll class with SSL set to none.

        Arguments:

        """

        cfg = Cfg2()
        mongo = mongo_libs.crt_coll_inst(cfg, "db", "tbl")

        self.assertFalse(mongo.ssl_client_ca)

    def test_rep_none_ssl(self):

        """Function:  test_rep_none_ssl

        Description:  Test mongo_class.RepSetColl class with SSL set to none.

        Arguments:

        """

        cfg = Cfg2(self.repset_hosts)
        mongo = mongo_libs.crt_coll_inst(cfg, "db", "tbl")

        self.assertFalse(mongo.ssl_client_ca)

    def test_coll_no_ssl(self):

        """Function:  test_coll_no_ssl

        Description:  Test the mongo_class.Coll class with no ssl.

        Arguments:

        """

        cfg = Cfg()
        mongo = mongo_libs.crt_coll_inst(cfg, "db", "tbl")

        self.assertFalse(mongo.ssl_client_ca)

    def test_rep_no_ssl(self):

        """Function:  test_rep_no_ssl

        Description:  Test the mongo_class.RepSetColl class with no ssl.

        Arguments:

        """

        cfg = Cfg(self.repset_hosts)
        mongo = mongo_libs.crt_coll_inst(cfg, "db", "tbl")

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.mongo_class.RepSetColl")
    def test_coll_mech_auth(self, mock_mongo):

        """Function:  test_coll_mech_auth

        Description:  Test with authentication mechanism passed.

        Arguments:

        """

        cfg = Cfg2()
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

    @mock.patch("mongo_libs.mongo_class.RepSetColl")
    def test_coll_no_mech_auth(self, mock_mongo):

        """Function:  test_coll_no_mech_auth

        Description:  Test with no authentication mechanism passed.

        Arguments:

        """

        cfg = Cfg()
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

    @mock.patch("mongo_libs.mongo_class.RepSetColl")
    def test_repset_mech_auth(self, mock_mongo):

        """Function:  test_repset_mech_auth

        Description:  Test with authentication mechanism passed.

        Arguments:

        """

        cfg = Cfg2(self.repset_hosts)
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

    @mock.patch("mongo_libs.mongo_class.RepSetColl")
    def test_repset_no_mech_auth(self, mock_mongo):

        """Function:  test_repset_no_mech_auth

        Description:  Test with no authentication mechanism passed.

        Arguments:

        """

        cfg = Cfg(self.repset_hosts)
        mock_mongo.return_value = True

        self.assertTrue(mongo_libs.crt_coll_inst(cfg, "db", "tbl"))

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
