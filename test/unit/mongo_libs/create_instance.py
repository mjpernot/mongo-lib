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
import mongo_class
import version

__version__ = version.__version__


class Cfg(object):

    """Class:  Cfg

    Description:  Class stub holder for Cfg class.

    Methods:
        __init__

    """

    def __init__(self):

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
        self.conf_file = "conf_file"


class Cfg2(object):

    """Class:  Cfg2

    Description:  Class stub holder for Cfg class with new attributes.

    Methods:
        __init__

    """

    def __init__(self):

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
        self.conf_file = "conf_file"
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
        test_set_ssl2
        test_set_ssl
        test_none_ssl2
        test_none_ssl
        test_no_ssl2
        test_no_ssl
        test_mech_auth2
        test_mech_auth
        test_no_mech_auth2
        test_no_mech_auth
        test_new_attributes4
        test_new_attributes3
        test_new_attributes2
        test_new_attributes
        test_repsetcoll_instance
        test_repset_instance
        test_slaverep_instance
        test_masterrep_instance
        test_rep_instance
        test_coll_instance
        test_db_instance
        test_server_instance

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
        self.use_uri = False
        self.use_arg = False
        self.auth_db = "admin"
        self.cfg = Cfg()
        self.cfg2 = Cfg2()
        self.cfg3 = Cfg3()
        self.use_uri2 = False
        self.use_arg2 = True
        self.auth_db2 = "mydatabase"
        self.auth_meth = "SCRAM-SHA-1"
        self.ssl_client_ca = "CAFile"

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl2(self, mock_load):

        """Function:  test_set_ssl2

        Description:  Test with SSL set.

        Arguments:

        """

        mock_load.return_value = self.cfg3
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.MasterRep)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl(self, mock_load):

        """Function:  test_set_ssl

        Description:  Test with SSL set.

        Arguments:

        """

        mock_load.return_value = self.cfg3
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Server)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl2(self, mock_load):

        """Function:  test_none_ssl2

        Description:  Test with SSL set to None.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.MasterRep)

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl(self, mock_load):

        """Function:  test_none_ssl

        Description:  Test with SSL set to None.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Server)

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_no_ssl2(self, mock_load):

        """Function:  test_no_ssl2

        Description:  Test with no SSL passed.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.MasterRep)

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_no_ssl(self, mock_load):

        """Function:  test_no_ssl

        Description:  Test with no SSL passed.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Server)

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_mech_auth2(self, mock_load):

        """Function:  test_mech_auth2

        Description:  Test with authentication mechanism passed.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.MasterRep)

        self.assertEqual(mongo.auth_mech, self.cfg2.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_mech_auth(self, mock_load):

        """Function:  test_mech_auth

        Description:  Test with authentication mechanism passed.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Server)

        self.assertEqual(mongo.auth_mech, self.cfg2.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_no_mech_auth2(self, mock_load):

        """Function:  test_no_mech_auth2

        Description:  Test with no authentication mechanism passed.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.MasterRep)

        self.assertEqual(mongo.auth_mech, self.auth_meth)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_no_mech_auth(self, mock_load):

        """Function:  test_no_mech_auth

        Description:  Test with no authentication mechanism passed.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Server)

        self.assertEqual(mongo.auth_mech, self.auth_meth)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_new_attributes4(self, mock_load):

        """Function:  test_new_attributes4

        Description:  Test with new use_uri, use_arg, and auth_db attributes.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.MasterRep)

        self.assertEqual(
            (mongo.use_uri, mongo.use_arg, mongo.auth_db),
            (self.use_uri2, self.use_arg2, self.auth_db2))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_new_attributes3(self, mock_load):

        """Function:  test_new_attributes3

        Description:  Test with new use_uri, use_arg, and auth_db attributes.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.MasterRep)

        self.assertEqual(
            (mongo.use_uri, mongo.use_arg, mongo.auth_db),
            (self.use_uri, self.use_arg, self.auth_db))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_new_attributes2(self, mock_load):

        """Function:  test_new_attributes2

        Description:  Test with new use_uri, use_arg, and auth_db attributes.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Server)

        self.assertEqual(
            (mongo.use_uri, mongo.use_arg, mongo.auth_db),
            (self.use_uri2, self.use_arg2, self.auth_db2))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_new_attributes(self, mock_load):

        """Function:  test_new_attributes

        Description:  Test with new use_uri, use_arg, and auth_db attributes.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Server)

        self.assertEqual(
            (mongo.use_uri, mongo.use_arg, mongo.auth_db),
            (self.use_uri, self.use_arg, self.auth_db))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_repsetcoll_instance(self, mock_load):

        """Function:  test_repsetcoll_instance

        Description:  Test creation of Mongo RepSetColl instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.RepSetColl)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_repset_instance(self, mock_load):

        """Function:  test_repset_instance

        Description:  Test creation of Mongo RepSet instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.RepSet)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_slaverep_instance(self, mock_load):

        """Function:  test_slaverep_instance

        Description:  Test creation of Mongo SlaveRep instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.SlaveRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_masterrep_instance(self, mock_load):

        """Function:  test_masterrep_instance

        Description:  Test creation of Mongo MasterRep instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.MasterRep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_rep_instance(self, mock_load):

        """Function:  test_rep_instance

        Description:  Test creation of Mongo Rep instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Rep)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_coll_instance(self, mock_load):

        """Function:  test_coll_instance

        Description:  Test creation of Mongo Coll instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Coll)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_db_instance(self, mock_load):

        """Function:  test_db_instance

        Description:  Test creation of Mongo DB instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.DB)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_server_instance(self, mock_load):

        """Function:  test_server_instance

        Description:  Test creation of Mongo Server instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance("cfg_file", "dir_path",
                                           mongo_class.Server)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))


if __name__ == "__main__":
    unittest.main()
