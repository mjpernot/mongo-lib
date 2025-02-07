# Classification (U)                            # pylint:disable=C0302

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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_libs                               # pylint:disable=E0401,C0413
import mongo_class                              # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class Cfg():                                    # pylint:disable=R0903

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


class Cfg2():                                   # pylint:disable=R0903

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
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class Cfg3():                                   # pylint:disable=R0903

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
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"
        self.auth_type = None
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class Cfg4():                                   # pylint:disable=R0903

    """Class:  Cfg4

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
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = "CAFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_phrase = "MyPhrase"
        self.auth_type = "SSL"
        self.tls_ca_certs = None
        self.tls_certkey = None
        self.tls_certkey_phrase = None


class Cfg5():                                   # pylint:disable=R0903

    """Class:  Cfg5

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
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = "TLS"
        self.tls_ca_certs = "tlsCAFile"
        self.tls_certkey = "tlsCertKeyFile"
        self.tls_certkey_phrase = "tlsCertKeyPhrase"

class Cfg6():                                   # pylint:disable=R0903

    """Class:  Cfg6

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
        self.direct_connect = False
        self.repset = "repset_name"
        self.conf_file = "conf_file"
        self.repset_hosts = repset_hosts
        self.db_auth = "db_name"
        self.auth_db = "mydatabase"
        self.auth_mech = "SCRAM-SHA-1"
        self.ssl_client_ca = None
        self.ssl_client_cert = None
        self.ssl_client_key = None
        self.ssl_client_phrase = None
        self.auth_type = "TLS"
        self.tls_ca_certs = "tlsCAFile"
        self.tls_certkey = "tlsCertKeyFile"
        self.tls_certkey_phrase = None


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_set_direct_connect_false
        test_set_tls_certkey_phrase8
        test_set_tls_certkey_phrase7
        test_set_tls_certkey_phrase6
        test_set_tls_certkey_phrase5
        test_set_tls_certkey_phrase4
        test_set_tls_certkey_phrase3
        test_set_tls_certkey_phrase2
        test_set_tls_certkey_phrase
        test_set_tls_certkey8
        test_set_tls_certkey7
        test_set_tls_certkey6
        test_set_tls_certkey5
        test_set_tls_certkey4
        test_set_tls_certkey3
        test_set_tls_certkey2
        test_set_tls_certkey
        test_set_tls_ca_certs8
        test_set_tls_ca_certs7
        test_set_tls_ca_certs6
        test_set_tls_ca_certs5
        test_set_tls_ca_certs4
        test_set_tls_ca_certs3
        test_set_tls_ca_certs2
        test_set_tls_ca_certs
        test_auth_type_tls
        test_auth_type_ssl
        test_auth_type_none
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
        self.auth_db = "admin"
        self.cfg = Cfg()
        self.cfg2 = Cfg2()
        self.cfg3 = Cfg3()
        self.cfg4 = Cfg4()
        self.cfg5 = Cfg5()
        self.cfg6 = Cfg6()
        self.auth_db2 = "mydatabase"
        self.auth_meth = "SCRAM-SHA-1"
        self.ssl_client_ca = "CAFile"
        self.auth_type = "TLS"
        self.tls_ca_certs = "tlsCAFile"
        self.tls_certkey = "tlsCertKeyFile"
        self.tls_certkey_phrase = "tlsCertKeyPhrase"

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_direct_connect_true(self, mock_load):

        """Function:  test_set_direct_connect_true

        Description:  Test with direct_connect set to True.

        Arguments:

        """

        self.cfg6.direct_connect = True

        mock_load.return_value = self.cfg6
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertTrue(mongo.direct_connect)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_direct_connect_false(self, mock_load):

        """Function:  test_set_direct_connect_false

        Description:  Test with direct_connect set to False.

        Arguments:

        """

        mock_load.return_value = self.cfg6
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSetColl)

        self.assertFalse(mongo.direct_connect)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase8(self, mock_load):

        """Function:  test_set_tls_certkey_phrase8

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSetColl)

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase7(self, mock_load):

        """Function:  test_set_tls_certkey_phrase7

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSet)

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase6(self, mock_load):

        """Function:  test_set_tls_certkey_phrase6

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.SlaveRep)

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase5(self, mock_load):

        """Function:  test_set_tls_certkey_phrase5

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Rep)

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase4(self, mock_load):

        """Function:  test_set_tls_certkey_phrase4

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Coll)

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase3(self, mock_load):

        """Function:  test_set_tls_certkey_phrase3

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.DB)

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase2(self, mock_load):

        """Function:  test_set_tls_certkey_phrase2

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey_phrase(self, mock_load):

        """Function:  test_set_tls_certkey_phrase

        Description:  Test with tls_certkey_phrase set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.tls_certkey_phrase, self.tls_certkey_phrase)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey8(self, mock_load):

        """Function:  test_set_tls_certkey8

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSetColl)

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey7(self, mock_load):

        """Function:  test_set_tls_certkey7

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSet)

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey6(self, mock_load):

        """Function:  test_set_tls_certkey6

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.SlaveRep)

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey5(self, mock_load):

        """Function:  test_set_tls_certkey5

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Rep)

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey4(self, mock_load):

        """Function:  test_set_tls_certkey4

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Coll)

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey3(self, mock_load):

        """Function:  test_set_tls_certkey3

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.DB)

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey2(self, mock_load):

        """Function:  test_set_tls_certkey2

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_certkey(self, mock_load):

        """Function:  test_set_tls_certkey

        Description:  Test with tls_certkey set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.tls_certkey, self.tls_certkey)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_ca_certs8(self, mock_load):

        """Function:  test_set_tls_ca_certs8

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSetColl)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_ca_certs7(self, mock_load):

        """Function:  test_set_tls_ca_certs7

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSet)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_ca_certs6(self, mock_load):

        """Function:  test_set_tls_ca_certs6

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.SlaveRep)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_ca_certs5(self, mock_load):

        """Function:  test_set_tls_ca_certs5

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Rep)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_ca_certs4(self, mock_load):

        """Function:  test_set_tls_ca_certs4

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Coll)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_ca_certs3(self, mock_load):

        """Function:  test_set_tls_ca_certs3

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.DB)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_ca_certs2(self, mock_load):

        """Function:  test_set_tls_ca_certs2

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_tls_ca_certs(self, mock_load):

        """Function:  test_set_tls_ca_certs

        Description:  Test with tls_ca_certs set.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.tls_ca_certs, self.tls_ca_certs)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_type_tls(self, mock_load):

        """Function:  test_auth_type_tls

        Description:  Test with auth_type set to TLS.

        Arguments:

        """

        mock_load.return_value = self.cfg5
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.auth_type, self.auth_type)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_type_ssl(self, mock_load):

        """Function:  test_auth_type_ssl

        Description:  Test with auth_type set to SSL.

        Arguments:

        """

        mock_load.return_value = self.cfg4
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.auth_type, "SSL")

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_auth_type_none(self, mock_load):

        """Function:  test_auth_type_none

        Description:  Test with auth_type set to None.

        Arguments:

        """

        mock_load.return_value = self.cfg3
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.auth_type, "SSL")

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl2(self, mock_load):

        """Function:  test_set_ssl2

        Description:  Test with SSL set.

        Arguments:

        """

        mock_load.return_value = self.cfg3
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_set_ssl(self, mock_load):

        """Function:  test_set_ssl

        Description:  Test with SSL set.

        Arguments:

        """

        mock_load.return_value = self.cfg3
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.ssl_client_ca, self.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl2(self, mock_load):

        """Function:  test_none_ssl2

        Description:  Test with SSL set to None.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_none_ssl(self, mock_load):

        """Function:  test_none_ssl

        Description:  Test with SSL set to None.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_no_ssl2(self, mock_load):

        """Function:  test_no_ssl2

        Description:  Test with no SSL passed.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_no_ssl(self, mock_load):

        """Function:  test_no_ssl

        Description:  Test with no SSL passed.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertFalse(mongo.ssl_client_ca)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_mech_auth2(self, mock_load):

        """Function:  test_mech_auth2

        Description:  Test with authentication mechanism passed.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertEqual(mongo.auth_mech, self.cfg2.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_mech_auth(self, mock_load):

        """Function:  test_mech_auth

        Description:  Test with authentication mechanism passed.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.auth_mech, self.cfg2.auth_mech)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_no_mech_auth2(self, mock_load):

        """Function:  test_no_mech_auth2

        Description:  Test with no authentication mechanism passed.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertEqual(mongo.auth_mech, self.auth_meth)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_no_mech_auth(self, mock_load):

        """Function:  test_no_mech_auth

        Description:  Test with no authentication mechanism passed.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.auth_mech, self.auth_meth)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_new_attributes4(self, mock_load):

        """Function:  test_new_attributes4

        Description:  Test with auth_db attributes.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertEqual(mongo.auth_db, self.auth_db2)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_new_attributes3(self, mock_load):

        """Function:  test_new_attributes3

        Description:  Test with kauth_db attributes.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

        self.assertEqual(mongo.auth_db, self.auth_db)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_new_attributes2(self, mock_load):

        """Function:  test_new_attributes2

        Description:  Test with auth_db attributes.

        Arguments:

        """

        mock_load.return_value = self.cfg2
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.auth_db, self.auth_db2)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_new_attributes(self, mock_load):

        """Function:  test_new_attributes

        Description:  Test with auth_db attributes.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(mongo.auth_db, self.auth_db)

    @mock.patch("mongo_libs.gen_libs.load_module")
    def test_repsetcoll_instance(self, mock_load):

        """Function:  test_repsetcoll_instance

        Description:  Test creation of Mongo RepSetColl instance.

        Arguments:

        """

        mock_load.return_value = self.cfg
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSetColl)

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
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.RepSet)

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
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.SlaveRep)

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
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.MasterRep)

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
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Rep)

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
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Coll)

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
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.DB)

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
        mongo = mongo_libs.create_instance(
            "cfg_file", "dir_path", mongo_class.Server)

        self.assertEqual(
            (mongo.name, mongo.user, mongo.japd, mongo.host, mongo.port,
             mongo.auth, mongo.conf_file),
            (self.name, self.user, self.japd, self.host, self.port, self.auth,
             self.conf_file))


if __name__ == "__main__":
    unittest.main()
